from ..src.consumer import Consumer
from ..src.id_factory import IdFctory
from ..util import config
from ..src.mongo_dal import MongoStore
from ..src.elastic_client import EsIndexer
import os
from ..util.logger import Logger

logger = Logger.get_logger()


class Stage2Manager:
    """
    a manager class for managing the stage2 workflow.
    """
    def __init__(self,
                 mongo_db: str = config.MONGO_DB,
                 mongo_uri: str = config.MONGO_URI,
                 es_host: str = config.ES_HOST,
                 es_index: str = config.ES_INDEX
                 ):
        self.id_factory = IdFctory()
        self.consumer = Consumer(config.KAFKA_TOPIC, config.KAFKA_BOOTSTRAP)
        self.mongo = MongoStore(mongo_uri=mongo_uri, db_name=mongo_db)
        self.es = EsIndexer(es_host, es_index)


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
            logger.error(f"error indexing {file_id} to mongo {e}")
            raise

    def manage_elastic(self)-> list[dict]:
        """
        manage indexing metadata into elastic.
        """
        docs = []
        try:
            for doc in self.consumer:
                doc["id"] = self.id_factory.create_hash(doc["file_path"])
                docs.append(doc)
            self.es.index_many(docs)
            logger.info(f"metadata indexed successfully")
            return docs
        except Exception as e:
            logger.error(f"error indexing into elastic {e}")
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
        x = self.manage_elastic()
        return x






if __name__ == "__main__":
    manager = Stage2Manager()
    manager.main()
    

    