from pymongo import MongoClient
from gridfs import GridFS
import logging

logger = logging.getLogger(__name__)

audio_file_path = 'path/to/your/audio.mp3'  # Replace with your audio file path
with open(audio_file_path, 'rb') as audio_file:
    file_id = fs.put(audio_file, filename='audio.mp3', content_type='audio/mpeg')
    print(f"Audio file stored with ID: {file_id}")