from ..src.words_recognizer import RiskScorer
from ..src.es_client import EsClientor
from ....tools.logger import Logger
from ..src.danger_list_creator import Base64Parser
from ....tools import config
logger = Logger.get_logger()


class RiskManager:
    """
    manager class for scoring docs danger and updating in es index.
    """
    def __init__(self):
        self.parser = Base64Parser()
        self.es = EsClientor(config.ES_HOST,config.ES_INDEX,config.ES_MAPPING)
        self.scorer = self._create_scoring()
    
    def _create_scoring(self):
        n_d_singel,m_d_pairs = self.parser.decode_flow(config.NOT_DANGER_LIST)
        dang_singel,danger_pairs = self.parser.decode_flow(config.DANGER_LIST)
        return RiskScorer(n_d_singel,dang_singel,m_d_pairs,danger_pairs)

    def score_dicts(self):
        docs = self.es.get_documents_limited(34)
        for doc in docs:
            
            

