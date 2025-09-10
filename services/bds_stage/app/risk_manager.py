from ..src.words_recognizer import RiskScorer
from ..src.es_client import EsClientor
from ....tools.logger import Logger

logger = Logger.get_logger()


class RiskManager:
    """
    manager class for scoring docs danger and updating in es index.
    """
    def __init__(self):
        self.scorer = RiskScorer()