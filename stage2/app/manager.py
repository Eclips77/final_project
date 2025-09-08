from src.consumer import Consumer
from src.id_factory import IdFctory
from util import config
from src.mongo_dal import MongoStore
from src.elastic_client import EsIndexer
import os
import logging


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class Stage2Manager:
    """
    a manager class for managing the stage2 workflow.
    """
    def __init__(self,
                 mongo_db: str = config.MONGO_DB,
                 mogo_uri: str = config.MONGO_URI,
                 es_host: str = config.ES_HOST,
                 es_index: str = config.ES_INDEX
                 ):
        self.id_factroy = IdFctory()
        self.consumer = Consumer(config.KAFKA_TOPIC,config.KAFKA_BOOTSTRAP,True)
        self.mongo = MongoStore(mongo_uri=mogo_uri, db_name=mongo_db)
        self.es = EsIndexer(es_host,es_index)

    
    def process_kafka_metadata(self) -> None:
        for meta in self.consumer:
            doc = dict(meta) 
            doc_id = doc.get("id") or doc.get("file_hash") or self.ids.new_uuid()
            doc["id"] = doc_id
            self.es.index_many([doc])
            self.consumer.commit()

    def ingest_local_file(self, file_path: str, basic_meta, prefer_hash: bool = True) -> str:
        file_id = self.ids.from_file(file_path) if prefer_hash else self.ids.new_uuid()
        filename = os.path.basename(file_path)
        aux = {"filename": filename}
        if basic_meta:
            aux.update(basic_meta)
        self.mongo.save_file(file_id=file_id, file_path=file_path, metadata=aux)
        doc = {"id": file_id, **aux}
        self.es.index_many([doc])
        return file_id
    


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


if __name__ == "__main__":
    manager = Stage2Manager()
    x = manager.read_file_paths(config.FILES_PATH)
    for z in x:
        print(z)