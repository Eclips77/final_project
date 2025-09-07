from pymongo import MongoClient
from gridfs import GridFS
import logging

logger = logging.getLogger(__name__)


client = MongoClient('mongodb://localhost:27017/')
db = client['audio_database']  
fs = GridFS(db)


audio_file_path = 'path/to/your/audio.mp3'  
with open(audio_file_path, 'rb') as audio_file:
    file_id = fs.put(audio_file, filename='audio.mp3', content_type='audio/mpeg')
    print(f"Audio file stored with ID: {file_id}")