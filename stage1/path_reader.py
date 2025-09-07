import os
import pathlib
import logging

logger = logging.getLogger(__name__)

class FileReader:
    @staticmethod
    def read_file_paths(directory:str)->list[str]:
        return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]


file_paths = FileReader.read_file_paths("C:/Users/brdwn/Desktop/my_projects/final_proj_data")
print(type(file_paths))

  

#     @staticmethod
#     def read_metadata():
#         pass

    

# BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# print(BASE_DIR)

# my_dir = Path("download (1).wav")
# print(my_dir.absolute())

# if __name__ == "__main__":
#     Reader.read_path("final_proj_data")