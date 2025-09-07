from pymongo import MongoClient
from gridfs import GridFS
import logging
from .mongo_client import DatabaseConnection
from ..config import MONGODB_COLLECTION
logger = logging.getLogger(__name__)


class MongoDal:
    """
    a class for push the audio files into mongo db
    """
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.database = self.db_connection.connect()
        self.collection = self.database[MONGODB_COLLECTION]
        self.fs = GridFS(database=self.database,collection=self.collection)


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



