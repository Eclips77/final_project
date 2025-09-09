import os
import stat
import datetime
from .logger import Logger
logger = Logger.get_logger()

class PathExtractor:
    @staticmethod
    def read_file_paths(directory:str)->list[str]:
        """
        a method that returns all the file pathes in a directory

        Args:

            directory path str.
        Returns:
        
                all the files pathes in the directory.
        """
        return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    @staticmethod
    def get_metadata(file_path:str)-> dict:
        """
        a method to get metadata about file.

        Args:
            file_path str.
        Return:
                dict of the meta data about the file.
        """
        if os.path.exists(file_path):
            file_stats = os.stat(file_path)
            logger.info(f"file exist in {file_path}")
            return {
                '_id': PathExtractor._create_hash(file_path),
                'size': file_stats.st_size,
                'permissions': stat.filemode(file_stats.st_mode),
                'create_date': datetime.date.fromtimestamp(file_stats.st_ctime),
                "file_name":os.path.basename(file_path),
                'file_path':file_path
            }
        else:
            logger.error(f"error create metadata from {file_path}")
            return {}
    
    @staticmethod
    def _create_hash(name:str):
        return hash(name)




