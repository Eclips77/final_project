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

 
    def update_document(self, index, doc_id, body):
        """
        Updates an existing document in a specified index.

        Args:
            index (str): The name of the Elasticsearch index.
            doc_id (str): The ID of the document to update.
            body (dict): A dictionary containing the fields to update or a script.

        Returns:
            dict or None: The update response if successful, otherwise None.
        """
        try:
            response = self.es.update(index=index, id=doc_id, body=body)
            if response:
                logger.info(f"doc {doc_id} updated")
            return response
        except Exception as e:
            logger.error(f"Error updating document: {e}")
            return None

    def partial_update_document(self,  doc_id, partial_doc):
        """
        Performs a partial update on a document.

        Args:
            index (str): The name of the Elasticsearch index.
            doc_id (str): The ID of the document to update.
            partial_doc (dict): A dictionary containing the fields to update.
        
        Returns:
            dict or None: The update response if successful, otherwise None.
        """
        return self.update_document(self.es_index, doc_id, {"doc": partial_doc})

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
                    }
                },
                size=limit  
            )
            documents = [hit['_source'] for hit in response['hits']['hits']]
            logger.info(f"retrieved {len(documents)} docs from elastic index")
            return documents
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return []
