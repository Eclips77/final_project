import os

# a variable to get the audio files path
FILES_PATH = os.getenv("FILES_PATH","C:/Users/brdwn/Desktop/my_projects/final_proj_data")
# a variable to get the mongo connection info
MONGO_URI = os.getenv("MONGO_URI","")
# a variable to get the elastic index
ES_INDEX = os.getenv("ES_INDEX","")
