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
        self.updater = ElasticUpdater(config.ES_HOST, config.ES_INDEX, ES_ID_FIELD, ES_TARGET_FIELD)

    def process_ids(self, file_ids: List[str]) -> List[Dict[str, str]]:
        """
        Processes a list of GridFS file ids: returns [{"id": str, "text": str}] after updating ES.
        """
        results: List[Dict[str, str]] = []
        for fid in file_ids:
            fp = self.fetcher.write_one(fid)
            tr = self.transcriber.transcribe_audio(fp["path"])
            self.updater.update_one(id_value=fp["id"], new_value=tr["text"], refresh=False)
            results.append({"id": fp["id"], "text": tr["text"]})
            try:
                os.remove(fp["path"])
            except Exception:
                pass
        self.updater.es.indices.refresh(index=self.updater.index)
        return results
