
from typing import Generator, Optional
from kafka import KafkaProducer, KafkaConsumer

class KafkaPubSub:
    """Generic Kafka publisher and subscriber using kafka-python."""

    def __init__(self, bootstrap_servers: str = "localhost:9092", group_id: str = "generic-consumer") -> None:
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, value_serializer=lambda v: str(v).encode("utf-8"))
        self.group_id = group_id

    def publish(self, topic: str, message: str) -> None:
        """Publish a message to a topic."""
        self.producer.send(topic, message)
        self.producer.flush()


def main() -> None:
    k = KafkaPubSub()
    print("KafkaPubSub initialized. Use publish/consume_iter with a running Kafka.")

if __name__ == "__main__":
    main()