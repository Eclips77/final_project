from typing import Dict, Iterator
import json
from kafka import KafkaConsumer


class Consumer:
    """
    consumer class 
    """

    def __init__(
        self,
        topic: str,
        bootstrap_servers: str,
        group_id: str,
        enable_auto_commit: bool = False,
    ) -> None:
        self._consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            enable_auto_commit=enable_auto_commit,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )

    def __iter__(self) -> Iterator[Dict]:
        """Iterate over incoming messages as dictionaries."""
        for msg in self._consumer:
            yield msg.value

    def commit(self) -> None:
        """Commit the current offset explicitly."""
        self._consumer.commit()

    def close(self) -> None:
        """Close the consumer."""
        self._consumer.close()
