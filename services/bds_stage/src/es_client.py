from elasticsearch import Elasticsearch
from ....tools.logger import Logger
from typing import List,Dict

logger = Logger.get_logger()

class EsClientor:
    def __init__(self, host :str,es_index : str,mapping: dict):
        """
        Initializes the ElasticsearchDocumentManager.

        Args:
            host (str): Elasticsearch host. Defaults to "localhost".
            port (int): Elasticsearch port. Defaults to 9200.
            cloud_id (str): Elastic Cloud ID (for cloud deployments).
            api_key (tuple): (id, api_key) for API key authentication.
        """
        self.es = Elasticsearch(hosts = [host])
        self.es_index = es_index
        self.es_mapping = mapping

    def update_document_by_field(self, field_name : str, field_value : str, update_data : str,target_field:str = "tts_data"):
        """
        update doc by field.
        Args:
            field_name (str)
            field_value (str)
            update_data (str)  data to update.


        """
        query = {
            "query": {"term": {field_name: {"value": field_value}}},
            "script": {
                "source": f"ctx._source['{target_field}'] = params.v",
                "lang": "painless",
                "params": {"v": update_data},
            },
        }
        try:
            response = self.es.update_by_query(index=self.es_index, body=query,refresh=True,)
            logger.info(f"doc {field_value} indexed.")
            return response
        except Exception as e:
            logger.error(f"error updating data {e}")
            raise

    def get_documents_limited(self,limit:int)-> List[Dict]:
        """
        Retrieves documents from an Elasticsearch index with a specified limit.

        Args:
            limit: The maximum number of documents to retrieve.

        Returns:
            A list of dictionaries, where each dictionary represents a document's _source.
        """
        try:
            response = self.es.search(
                index=self.es_index,
                body={
                  "query": {
                        "match_all": {} 
                    },
                    "_source": ["id","text"],
                    "size": limit                
                }
            )
            documents = [hit['_source'] for hit in response['hits']['hits']]
            logger.info(f"retrieved {len(documents)} docs from elastic index")
            return documents
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return []