from typing import Dict, Iterator
from bson import json_util
from kafka import KafkaConsumer
from ..util import config
from ..util.logger import Logger

logger = Logger.get_logger()

class Consumer:
    """
    consumer class for Kafka metadata consumption
    """

    def __init__(
        self,
        topic: str,
        bootstrap_servers: str,
        group_id: str = None,
        enable_auto_commit: bool = False,):

        self._consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            enable_auto_commit=enable_auto_commit,
            auto_offset_reset='earliest',
            value_deserializer=lambda v: json_util.loads(v.decode("utf-8")),
        )
        logger.info(f"Kafka consumer initialized for topic: {topic}, group: {group_id}")

    def __iter__(self) -> Iterator[Dict]:
        """Iterate over incoming messages as dictionaries."""
        try:
            for msg in self._consumer:
                logger.debug(f"Received message from partition {msg.partition}, offset {msg.offset}")
                yield msg.value
        except Exception as e:
            logger.error(f"Error consuming message: {e}")
            raise

    def commit(self) -> None:
        """Commit the current offset explicitly."""
        try:
            self._consumer.commit()
            logger.debug("Offset committed successfully")
        except Exception as e:
            logger.error(f"Error committing offset: {e}")
            raise

    def close(self) -> None:
        """Close the consumer."""
        try:
            self._consumer.close()
            logger.info("Kafka consumer closed successfully")
        except Exception as e:
            logger.error(f"Error closing consumer: {e}")
            raise


if __name__ == "__main__":
    consumer = Consumer(config.KAFKA_TOPIC,config.KAFKA_BOOTSTRAP)
    for msg in consumer:
        print(msg)