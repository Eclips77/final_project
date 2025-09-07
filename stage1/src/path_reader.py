import os
import stat
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
    def get_metadata(file_path:str)-> dict:
        """
        a method to get metadata about file.

        Args:
            filepath str.
        Return:
                dict of the meta data about the file.
        """
        if os.path.exists(file_path):
            file_stats = os.stat(file_path)
            logger.info(f"file exist in {file_path}")
            return {
                'size': file_stats.st_size,
                'permissions': stat.filemode(file_stats.st_mode),
                'create_date': datetime.datetime.fromtimestamp(file_stats.st_ctime),
                "file_name":os.path.basename(file_path),
                'file_path':file_path
            }
        else:
            logger.error(f"error create metadata from {file_path}")
            return {}




