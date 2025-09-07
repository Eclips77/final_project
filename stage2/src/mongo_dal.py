from gridfs import GridFS
import logging
from .mongo_client import DatabaseConnection
from .. import config
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

class MongoDal:
    """
    a class for push the audio files into mongo db
    """
    def __init__(self,mongo_collection:str):
        self.db_connection = DatabaseConnection()
        self.database = self.db_connection.connect()
        self.collection = self.database[mongo_collection]
        self.fs = GridFS(database=self.database,collection=self.collection)
        logger.info("connection created seccssesfuly")


    def push_to_mongo(self,file_path:str)-> str:
        """
        Push an audio file into the db

        Args:
            file_path str.
        Returns:
                the document id to improve success
        """
        with open (file_path,'rb') as audio_file:
            file_id = self.fs.put(audio_file,filename=audio_file, content_type='audio/mpeg')
            return file_id



if __name__ == "__main__":
    dal = MongoDal(config.MONGODB_COLLECTION)
    dal.push_to_mongo(config.FILES_PATH+"download (1).wav")