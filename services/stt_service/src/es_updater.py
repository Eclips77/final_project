from elasticsearch import Elasticsearch
from ....tools.logger import Logger
logger = Logger.get_logger()

class ElasticUpdater:
    def __init__(self, host:str,es_index: str):

        self.es = Elasticsearch(hosts=[host])
        self.es_index = es_index

    def update_document_by_field(self, field_name : str, field_value : str, update_data : str):
        """
        update doc by field.
        Args:
            field_name (str)
            field_value (str)
            update_data (str)  data to update.


        """
        query = {
            "query": {
                "match": {
                    field_name: field_value
                }
            },
            "script": {
                "source": "ctx._source.tts_data = params.update_data",
                "lang": "painless",
                "params": {
                    "update_data": update_data
                }
            }
        }
        try:
            response = self.es.update_by_query(index=self.es_index, body=query,refresh=True,)
            logger.info(f"doc {field_value} indexed.")
            return response
        except Exception as e:
            logger.error(f"error updating data {e}")
            raise
            

