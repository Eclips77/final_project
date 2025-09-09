from ...tools import config
from .src.kafka_publisher import KafkaPubSub
from ...tools.meta_data_creator import FileMetadataService
from ...tools.logger import Logger

logger = Logger.get_logger()


class Stage1Manager:
    """
    a manager class for the flow of stage 1.
    """
    def __init__(self):
        self.publisher = KafkaPubSub(config.KAFKA_BOOTSTRAP)
        self.topic = config.KAFKA_TOPIC
        self.data_creator = FileMetadataService(config.DATA_DIR)
        self.data = None
    
    def main(self):
        """
        manage the meta data creator service

        create the meta data and publish it into kafka.
        """
        try:
            self.data = self.data_creator.get_all_metadata()
            logger.info("files pathes loaded!.")
            if self.data:
                for meta in self.data:
                    self.publisher.publish(config.KAFKA_TOPIC,meta)
                logger.info(f"Published data into topic {config.KAFKA_TOPIC}")
        except Exception as e:
            logger.error(f"Error in main loop: {e}")




if __name__ == "__main__":
    manager = Stage1Manager()
    manager.main()