from typing import Dict
from pymongo import MongoClient
import gridfs
import tempfile
from ....tools.logger import Logger
logger = Logger.get_logger()

class GridFSToTempWav:
    """
    Streams a WAV file from GridFS to a temporary file and returns {"id": str, "path": str}.
    """
    def __init__(self, mongo_uri: str, db_name: str, bucket: str = "fs") -> None:
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db, collection=bucket)



    def write_one(self, file_id: str) -> Dict[str, str]:
        """
        Writes a single WAV file by GridFS _id to a temporary file.

        Args:
            file_id: GridFS file _id as string.

        Returns:
            Dict with the file id and temp file path.
        """
        try:
            gf = self.fs.get(file_id)
            logger.info(f"chunk found {file_id}")
            tmp = tempfile.NamedTemporaryFile(prefix=f"{file_id}_", suffix=".wav", delete=False)
            with tmp as f:
                while True:
                    chunk = gf.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
            return {"id": str(file_id), "path": tmp.name}
        except Exception as e:
            logger.error(f"error reriving chunk {e}")
            raise

# if __name__ == "__main__":
#     g = GridFSToTempWav(config.MONGO_URI,config.MONGO_DB)
#     x = g.write_one("1f7c38c5a0c68696624a2520e2838b5a8c47b30bdcb2ad46cfe65183c7750c15")
#     print(x)