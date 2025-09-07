from pymongo import MongoClient
from gridfs import GridFS
import logging
from .mongo_client import DatabaseConnection
logger = logging.getLogger(__name__)


class MongoDal:
    """
    a class for push the audio files into mongo db
    """
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.database = self.db_connection.connect()
        self.collection = self.database[config.MONGODB_COLLECTION]


client = MongoClient('mongodb://localhost:27017/')
db = client['audio_database']  
fs = GridFS(db)


audio_file_path = 'path/to/your/audio.mp3'  
with open(audio_file_path, 'rb') as audio_file:
    file_id = fs.put(audio_file, filename='audio.mp3', content_type='audio/mpeg')
    print(f"Audio file stored with ID: {file_id}")