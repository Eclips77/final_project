from kafka import KafkaConsumer
# from pymongo import MongoClient, ASCENDING, errors
from datetime import datetime, timezone
from .. import config
import json
class InterestingConsumerService:
    def __init__(self) -> None:
        self._consumer = KafkaConsumer(
            config.KAFKA_TOPIC,
            bootstrap_servers=config.KAFKA_BOOTSTRAP,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            enable_auto_commit=False,
            # auto_offset_reset=config.AUTO_OFFSET_RESET,
            # session_timeout_ms=config.SESSION_TIMEOUT_MS,
        )
  

    @property
    def consumer(self) -> KafkaConsumer:
        return self._consumer

    @property
    def collection(self):
        return self._coll

   