from faster_whisper import WhisperModel
from ....tools.logger import Logger
import os
from ....tools import config
logger = Logger.get_logger()


class AudioProcessor:
    """
    A  class to process audio files using the Whisper model for transcription.
    """
    def __init__(self,model_path):
        """
        Initializes the AudioProcessor with a Whisper model.
        Args:
            model_size (str): The size of the Whisper model.
            device (str): The device to run the model on.
            compute_type (str): The compute type for the model.
        """
        self.model = WhisperModel(model_path, device="cpu", compute_type="int8")
        logger.info(f"Whisper model loaded)")

    def transcribe_audio(self, audio_path: str, task="transcribe", beam_size=5, vad_filter=True):
        """
        Transcribes an audio file.
        Args:
            audio_path (str): The path to the audio file.
            task (str): The task for the model ("transcribe" or "translate").
            beam_size (int): The beam size for decoding.
            vad_filter (bool): Whether to use the VAD filter.
        Returns:
            A str that contains the text transcribed.
        """
        try:
            segments,info = self.model.transcribe(
                str(audio_path),
                task=task,
                beam_size=beam_size,
                vad_filter=vad_filter
            )
            text = "".join(seg.text for seg in segments)
            return text
        except Exception as e:
            logger.error(f"transcribe failed: {e}")
            raise

