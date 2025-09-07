from . import config
from src.kafka_publisher import KafkaPubSub
from src.path_reader import FileReader
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class Stage1Manager:
    """
    a manager class for the flow of stage 1.
    """
    def __init__(self):
        pass