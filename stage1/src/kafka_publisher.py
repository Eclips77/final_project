from kafka import KafkaProducer
from bson import json_util

class KafkaPubSub:
    """Generic Kafka publisher and subscriber using kafka-python."""

    def __init__(self, bootstrap_servers: str, group_id: str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, value_serializer=lambda v: json_util.dumps(v).encode('utf-8'))
        self.group_id = group_id

    def publish(self, topic: str, message: str) -> None:
        """Publish a message to a topic."""
        self.producer.send(topic, message)
        self.producer.flush()


# def main() -> None:
#     k = KafkaPubSub()
#     k.publish()

# if __name__ == "__main__":
#     main()