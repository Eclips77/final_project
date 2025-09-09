import os
import stat
import datetime
import hashlib
from .logger import Logger
logger = Logger.get_logger()
from typing import List, Dict, Any

class FileMetadataService:
    def __init__(self, directory: str):
        self.directory = directory

    def list_files(self) -> List[str]:
        """
        get the files path.

        Returns:
                List[str] of the files paths in a directory.
        """
        return [
            os.path.join(self.directory, f)
            for f in os.listdir(self.directory)
            if os.path.isfile(os.path.join(self.directory, f))
        ]

    def _create_hash_id(self, path: str) -> str:
        """
        creates a unique id from file path.

        Args:
            file path (str).

        Returns:
                unique id number (str).
        """
        return hashlib.sha256(path.encode("utf-8")).hexdigest()

    def get_metadata(self, path: str) -> Dict[str, Any]:
        """
        create a dict of the metat data about file.

        Args:
             file path (str) .
        Return:
                dict with all the meta data.

        """
        stats = os.stat(path)
        return {
            "id": self._create_hash_id(path),
            "file_path": path,
            "size": stats.st_size,
            "create_date": datetime.date.fromtimestamp(stats.st_ctime,).isoformat(),
            "modified": stats.st_mtime,
            "file_name":os.path.basename(path),
            "permissions": stat.filemode(stats.st_mode),
        }

    def get_all_metadata(self) -> List[Dict[str, Any]]:
        """
        return a list of dicts with the meta data.
        """
        return [self.get_metadata(f) for f in self.list_files()]


# if __name__ == "__main__":
#     drt = FileMetadataService("C:/Users/brdwn/Desktop/my_projects/final_proj_data")
#     x = drt.get_all_metadata()
#     z = x[0]
#     print(type(z["create_date"]))
