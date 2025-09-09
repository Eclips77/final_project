from typing import Dict, List
from elasticsearch import Elasticsearch, helpers




class ElasticUpdate:
    """
    updated exist data in elastic index.
    """
    def __init__(self, host: str , index_name: str):
        self.es = Elasticsearch(hosts=[host])
        self.index = index_name
