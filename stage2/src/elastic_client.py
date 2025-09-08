from typing import Dict, List
from elasticsearch import Elasticsearch, helpers
from ..util.logger import Logger

logger = Logger.get_logger()

class EsIndexer:
    """Indexes metadata dictionaries into Elasticsearch under stable IDs."""

    def __init__(self, host: str , index_name: str):
        self.es = Elasticsearch(hosts=[host])
        self.index = index_name
        self.ensure_index()

    def ensure_index(self):
        """Create the index if it does not exist."""
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index, body=self.mapping)
            logger.info(f"index {self.index} create successfully.")

    def index_many(self, docs: List[Dict]):
        actions = []
        for d in docs:
            doc_id = d.get("_id")
            if not doc_id:
                logger.error("Each document must include an '_id' field.")
                raise ValueError("Each document must include an '_id' field.")
            actions.append({
                "_op_type": "index",
                "_index": self.index,
                "_id": doc_id,
                "_source": d,
            })
        if actions:
            helpers.bulk(self.es, actions)
            logger.info("docs indexed successfully.")
