import os 
from typing import List

# a str path to the data directory
DATA_DIR_PATH:str = os.getenv("DATA_DIR_PATH","C:/Users/brdwn/Desktop/my_projects/final_proj_data")

# a list[str] of the connection to kafka parts
KAFKA_BOOTSTRAP: List[str] = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092").split(",")

# str of the topic name
TOPIC: str = os.getenv("KAFKA_TOPIC","metadata")

