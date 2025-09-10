from typing import List, Dict
import os
from ....tools import config
from ..src.mongo_fetcher import GridFSToTempWav
from ..src.converter import AudioProcessor
from ..src.es_updater import ElasticUpdater
from ....tools.meta_data_creator import FileMetadataService

class TtsManager:
    """
    Pulls WAV from GridFS -> transcribes with Faster-Whisper -> updates transcript in Elasticsearch.
    """
    def __init__(self) -> None:
        self.fetcher = GridFSToTempWav(config.MONGO_URI,config.MONGO_DB)
        self.transcriber = AudioProcessor(model_path = config.MODEL_PATH_ENV_VAR)
        self.updater = ElasticUpdater(config.ES_HOST, config.ES_INDEX)
        self.file_service = FileMetadataService(config.DATA_DIR)
        self.ids = self.file_service.retrive_all_ids()


    def process_ids(self, file_ids: List[str]) -> List[Dict[str, str]]:
        """
        Processes a list of GridFS file ids: returns [{"id": str, "text": str}] after updating ES.
        """
        results: List[Dict[str, str]] = []
        for fid in file_ids:
            temp_file = self.fetcher.write_one(fid)
            transcription_result = self.transcriber.transcribe_audio(temp_file["path"])
            self.updater.update_document_by_field("id",temp_file["id"],transcription_result)
            results.append({"id": temp_file["id"], "text": transcription_result})
            try:
                os.remove(temp_file["path"])
            except Exception:
                pass
        self.updater.es.indices.refresh(index=self.updater.es_index)
        return results
    
    def main(self):
        self.process_ids(self.ids)


if __name__ == "__main__":
    tts_manager = TtsManager()
    tts_manager.main()

  