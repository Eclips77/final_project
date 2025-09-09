from faster_whisper import WhisperModel
from ...tools.logger import Logger
logger = Logger.get_logger()


class AudioProcessor:
    """
    A  class to process audio files using the Whisper model for transcription.
    """
    def __init__(self, model_size="small", device="cpu", compute_type="int8"):
        """
        Initializes the AudioProcessor with a Whisper model.
        Args:
            model_size (str): The size of the Whisper model.
            device (str): The device to run the model on.
            compute_type (str): The compute type for the model.
        """
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
        logger.info(f"Whisper model loaded: {model_size} ({device}, {compute_type})")

    def transcribe_audio(self, audio_path: str, task="transcribe", beam_size=5, vad_filter=True):
        """
        Transcribes an audio file.
        Args:
            audio_path (str): The path to the audio file.
            task (str): The task for the model.
            beam_size (int): The beam size for decoding.
            vad_filter (bool): Whether to use the VAD filter.
        Returns:
            A str of the transcription info.
        """

        logger.info(f"Transcribing {audio_path}...")
        segments, info = self.model.transcribe(
            str(audio_path),
            task=task,
            beam_size=beam_size,
            vad_filter=vad_filter
        )
        logger.info(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")
        transcription = ""
        for segment in segments:
            transcription += segment.text + " "
        return transcription.strip()

