import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..",".."))
DATA_DIR = os.path.join(BASE_DIR, "final_proj_data")

# a variable to get the audio files path
FILES_PATH : str = os.getenv("FILES_PATH",DATA_DIR)
# a variable to get the mongo connection info
MONGO_URI : str = os.getenv("MONGO_URI","mongodb://localhost:27017")
# a variable to get the mongo database name
MONGO_DB : str = os.getenv("MONGO_DB","audioDB")
# a variable to get the elastic index
ES_INDEX : str = os.getenv("ES_INDEX","audioMetaData")
# a variable to get the db collection
MONGODB_COLLECTION : str = os.getenv("MONGODB_COLLECTION","podcasts")
# a variable to get the kafka topic
KAFKA_TOPIC : str = os.getenv("KAFKA_TOPIC","metadata")
# a variable to get the server bootstrap
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092").split(",")
# a variable to get the kafka consumer group
KAFKA_CONSUMER_GROUP: str = os.getenv("KAFKA_CONSUMER_GROUP", "metadata_group")
# a variable to get the elastic connection info
ES_HOST: str = os.getenv("ES_HOST","http://localhost:9200")


ES_MAPPING : dict = {

}



