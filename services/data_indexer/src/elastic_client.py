from typing import Dict, List
from elasticsearch import Elasticsearch, helpers
from ....tools.logger import Logger

logger = Logger.get_logger()

class EsIndexer:
    """Indexes metadata dictionaries into Elasticsearch under stable IDs."""

    def __init__(self, host: str , index_name: str,mapping:dict):
        self.es = Elasticsearch(hosts=[host])
        self.index = index_name
        self.mapping = mapping

        self.ensure_index()

    def ensure_index(self):
        """Create the index if it does not exist."""
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index, body=self.mapping)
            logger.info(f"index {self.index} create successfully.")

    def index_doc(self, document):
        try:
            response = self.es.index(index=self.index,document=document)
            logger.info(f"doc {document} indexed.")
            return response
        except Exception as e:
            logger.error(f"Error indexing document: {e}")
            return None
