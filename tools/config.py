import os
from typing import List

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..")) # i removed one ".."
DATA_DIR = os.path.join(BASE_DIR, "final_proj_data")

# a variable to get the audio files path
FILES_PATH : str = os.getenv("FILES_PATH",DATA_DIR)
# a variable to get the mongo connection info
MONGO_URI : str = os.getenv("MONGO_URI","mongodb://localhost:27017")
# a variable to get the mongo database name
MONGO_DB : str = os.getenv("MONGO_DB","audioDB")
# a variable to get the elastic index
ES_INDEX : str = os.getenv("ES_INDEX","audio_meta_data")
# a variable to get the db collection
MONGODB_COLLECTION : str = os.getenv("MONGODB_COLLECTION","podcasts")
# a variable to get the kafka topic
KAFKA_TOPIC : str = os.getenv("KAFKA_TOPIC","metadata")
# a variable to get the server bootstrap
KAFKA_BOOTSTRAP: List[str] = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092").split(",")
# a variable to get the kafka consumer group
KAFKA_CONSUMER_GROUP: str = os.getenv("KAFKA_CONSUMER_GROUP", "metadata_group")
# a variable to get the elastic connection info
ES_HOST: str = os.getenv("ES_HOST","http://localhost:9200")


ES_MAPPING = {
  "mappings": {
    "properties": {
      "id": { 
        "type": "keyword"
      },
      "size": {
        "type": "text",
        "fields": {
          "raw": { 
            "type": "keyword", 
            "ignore_above": 32766 
          }
        }
      },
      "permissions": { 
        "type": "keyword" 
      },
      "create_date": { 
        "type": "date",
        "format":"strict_date_optional_time||epoch_millis"
      }, 
      "file_name": { 
        "type": "keyword"
      },
      "file_path": { 
        "type": "keyword" 
      },
      "tts_data":{
          "type":"text"
      }
    }
  }
}




