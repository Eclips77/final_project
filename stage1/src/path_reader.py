import os
from pathlib import Path
import logging
import datetime
logger = logging.getLogger(__name__)

class FileReader:
    @staticmethod
    def read_file_paths(directory:str)->list[str]:
        """
        a method that returns all the file pathes in a directory
        Args:
            directory path : str.
        Returns:
                all the files pathes in the directory.
        """
        return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    @staticmethod
    def files_metadata(file_pathes: list[str]):
        """
        a method for return metadata about files.
        """
        for path in file_pathes:
            path = Path(path)
            metadata = {
                "size":path.stat().st_size,
                "create_time":datetime.datetime.fromtimestamp(path.stat().st_ctime),
                "name":path.name
            }
        return list(metadata)
        


x = FileReader.files_metadata("C:/Users/brdwn/Desktop/my_projects/final_proj_data")
print(x)


# file_path = Path("C:/Users/brdwn/Desktop/my_projects/final_proj_data/download (1).wav")
            
# file_stats = file_path.stat()

  
# print(f"File Size: {file_stats.st_size} bytes") # size of a file
# print(f"Last Modified: {datetime.datetime.fromtimestamp(file_stats.st_mtime)}") # last file modified
# print(f"Creation Time (or Metadata Change): {datetime.datetime.fromtimestamp(file_stats.st_ctime)}") # creation time of a file
# print(f"{file_path.name   }")