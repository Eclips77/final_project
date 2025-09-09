from ..src.consumer import Consumer
from ....tools.id_factory import IdFctory
from ....tools import config
from ..src.mongo_dal import MongoStore
from ..src.elastic_client import EsIndexer
import os
from ....tools.logger import Logger

logger = Logger.get_logger()


class Stage2Manager:
    """
    a manager class for managing the stage2 workflow.
    """
    def __init__(self,
                 mongo_db: str = config.MONGO_DB,
                 mongo_uri: str = config.MONGO_URI,
                 es_host: str = config.ES_HOST,
                 es_index: str = config.ES_INDEX,
                 es_mapping: dict = config.ES_MAPPING
                 ):
        self.id_factory = IdFctory()
        self.consumer = Consumer(config.KAFKA_TOPIC, config.KAFKA_BOOTSTRAP,config.KAFKA_CONSUMER_GROUP)
        self.mongo = MongoStore(mongo_uri=mongo_uri, db_name=mongo_db)
        self.es = EsIndexer(es_host, es_index,es_mapping)


    def manage_mongo(self,files_pathes:list[str]):
        """
        manage the data files and inde to mongo.
        """
        try:
            for path in files_pathes:
                file_id = self.id_factory.create_hash(path)
                self.mongo.save_file(file_id,path)
                logger.info(f"file {file_id} indexed successfully")
        except Exception as e:
            logger.error(f"Error indexing to mongo {e}")
            raise

    def manage_elastic(self):
        """
        manage indexing metadata into elastic.
        """
        try:
            for doc in self.consumer:
                self.es.index_doc(doc)
                logger.info(f"metadata indexed successfully")
        except Exception as e:
            logger.error(f"Error indexing into elastic {e}")
            raise

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


    def main(self):
        pathes = self.read_file_paths(config.FILES_PATH)
        self.manage_mongo(pathes)
        self.manage_elastic()


if __name__ == "__main__":
    manager = Stage2Manager()
    manager.main()
    

    