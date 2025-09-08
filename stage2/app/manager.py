from ..src.consumer import Consumer
from ..src.id_factory import IdFctory
from .. import config
from ..src.mongo_dal import MongoStore

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
        self.mongo = MongoStore(mongo_uri=mongo_uri, db_name=mongo_db)
