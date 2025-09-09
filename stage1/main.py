from . import config
from .src.kafka_publisher import KafkaPubSub
from .src.path_reader import FileReader
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
        self.publisher = KafkaPubSub(config.KAFKA_BOOTSTRAP)
        self.topic = config.TOPIC
        self.data = None
    
    def main(self):
        try:
            self.data = FileReader.read_file_paths(config.DATA_DIR_PATH)
            logger.info("files pathes loaded!.")
            for meta in self.data:
                data_to_pub = FileReader.get_metadata(meta)
                self.publisher.publish(config.TOPIC,data_to_pub)
            logger.info(f"Published data into topic {config.TOPIC}")

        except Exception as e:
            logger.error(f"Error in main loop: {e}")




if __name__ == "__main__":
    manager = Stage1Manager()
    manager.main()