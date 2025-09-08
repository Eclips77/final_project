from ..src.consumer import Consumer
from ..src.id_factory import IdFctory
from .. import config
# from ..src import 

import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class Stage2Manager:
    """
    a manager class for managing the stage2 workflow.
    """
    def __init__(self,
                 mongo_db: str,
                 mogo_uri: str,
                 es_host: str,
                 es_index: str
                 ):
        self.id_factroy = IdFctory()
        self.consumer = Consumer(config.KAFKA_TOPIC,config.KAFKA_BOOTSTRAP,True)
        