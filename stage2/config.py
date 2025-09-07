import os

# a variable to get the audio files path
FILES_PATH : str = os.getenv("FILES_PATH","C:/Users/brdwn/Desktop/my_projects/final_proj_data") # temporary! remember to change it.
# a variable to get the mongo connection info
MONGO_URI : str = os.getenv("MONGO_URI","mongodb://localhost:27017")
# a variable to get the mongo database name
MONGO_DB : str = os.getenv("MONGO_DB","audioDB")
# a variable to get the elastic index
ES_INDEX : str = os.getenv("ES_INDEX","audioMetaData")
MONGODB_COLLECTION : str = os.getenv("MONGODB_COLLECTION","podcasts")
