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

    
    def 
