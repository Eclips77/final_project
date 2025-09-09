from typing import List, Dict
import os
from ....tools import config
from ..src.mongo_fetcher import GridFSToTempWav
from ..src.converter import AudioProcessor
from ..src.es_updater import ElasticUpdater
from ....tools.meta_data_creator import FileMetadataService

class ASRPipeline:
    """
    Pulls WAV from GridFS → transcribes with Faster-Whisper → updates transcript in Elasticsearch.
    """
    def __init__(self) -> None:
        self.fetcher = GridFSToTempWav(config.MONGO_URI,config.MONGO_DB)
        self.transcriber = AudioProcessor()
        self.updater = ElasticUpdater(config.ES_HOST, config.ES_INDEX)
        self.file_service = FileMetadataService(config.DATA_DIR)
        self.ids = self.file_service.retrive_all_ids()

    def process_ids(self)-> List[str] :
        """
        Processes a list of GridFS file ids: returns [{"id": str, "text": str}] after updating ES.
        """
        temp_files = [self.fetcher.write_one(id) for id in self.ids]
        temp_files = [self.transcriber.transcribe_audio(file["path"])for file in temp_files]
        return temp_files

    def tts_manager(self):


    def es_update_manager(self,field_name:str = "id"):
        for id in self.ids:
            self.updater.update_document_by_field(field_name,id,"ddd")


  