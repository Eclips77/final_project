from elasticsearch import Elasticsearch
from ....tools.logger import Logger
logger = Logger.get_logger()

class ElasticUpdater:
    def __init__(self, host:str,es_index: str):

        self.es = Elasticsearch(hosts=[host])
        self.es_index = es_index

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
            
     
