from kafka import KafkaProducer
from bson import json_util
from typing import List
from ...tools.logger import Logger
logger = Logger.get_logger()
class KafkaPubSub:
    """Generic Kafka publisher and subscriber using kafka-python."""

    def __init__(self, bootstrap_servers: List[str]) -> None:
        self.bootstrap_servers = bootstrap_servers
        self._producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, value_serializer=lambda v: json_util.dumps(v).encode('utf-8'))
        logger.info(f"Kafka Producer initialized with bootstrap servers: {bootstrap_servers}")

    @property
    def producer(self):
        return self._producer

    def publish(self, topic: str, message: dict):
        """
        Publish a message to a Kafka topic
        
        Args:
            topic (str): Kafka topic name
            message (dict): Message to send
        """
        try:
            for m in message:
                self._producer.send(topic, value=m)
            self._producer.flush()
            logger.info(f"Message published to topic '{topic}': {message}")
        except Exception as e:
            logger.error(f"Failed to publish message to topic '{topic}': {e}")
            raise RuntimeError(f"Failed to publish message to topic '{topic}': {e}")


# def main() -> None:
#     k = KafkaPubSub()
#     k.publish()

# if __name__ == "__main__":
#     main()