from typing import List, Dict
import os
from ....tools import config
from ..src.mongo_fetcher import GridFSToTempWav
from ..src.converter import AudioProcessor
from ..src.es_updater import ElasticUpdater

class ASRPipeline:
    """
    Pulls WAV from GridFS → transcribes with Faster-Whisper → updates transcript in Elasticsearch.
    """
    def __init__(self) -> None:
        self.fetcher = GridFSToTempWav(config.MONGO_URI,config.MONGO_DB)
        self.transcriber = AudioProcessor()
        self.updater = ElasticUpdater(config.ES_HOST, config.ES_INDEX)

    def process_ids(self, file_ids: List[str]) :
        """
        Processes a list of GridFS file ids: returns [{"id": str, "text": str}] after updating ES.
        """
        

  