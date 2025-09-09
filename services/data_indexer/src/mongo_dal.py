from pymongo import MongoClient
import gridfs
from ....tools.logger import Logger

logger = Logger.get_logger()

class MongoStore:
    """
    Stores audio files in MongoDB using GridFS.
    """

    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def exists(self, file_id: str) -> bool:
        """Return True if a file with the given ID exists in GridFS."""
        return self.db.fs.files.find_one({"_id": file_id}) is not None

    def save_file(self, file_id: str, file_path: str) -> str:
        """
        save a file into the db.

        Args:
            file_id , file_path .
        
        Return:
                the file id (int)
        """
        if self.exists(file_id):
            logger.info(f"file id alredy exsist {file_id}")
            return file_id  
        with open(file_path, "rb") as f:
            self.fs.put(f, _id=file_id, filename=file_path,)
            logger.info(f"file stored successfully")
        return file_id

    def get_file(self, file_id: int) -> bytes:
        """Retrieve a file's raw bytes by ID."""
        file_obj = self.fs.get(file_id)
        return file_obj.read()
