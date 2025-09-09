from faster_whisper import WhisperModel

class SpeechToTextConverter:
    """
    A class to convert speech to text using the Faster Whisper model.
    """

    def __init__(self, model_size="small", device="cpu", compute_type="float32"):
        """
        Initializes the SpeechToTextConverter with a specified Faster Whisper model.

        Args:
            model_size (str): The size of the Whisper model to use (e.g., "tiny", "base", "small", "medium", "large-v2").
            device (str): The device to run the model on ("cpu" or "cuda").
            compute_type (str): The compute type for the model (e.g., "float32", "int8_float16").
        """
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def transcribe_audio(self, audio_path, language=None, vad_filter=True, **kwargs):
        """
        Transcribes an audio file to text.

        Args:
            audio_path (str or np.ndarray): Path to the audio file or a NumPy array representing the audio.
            language (str, optional): The language of the audio (e.g., "en" for English).
                                      If None, the model will attempt to detect the language.
            vad_filter (bool): Whether to apply voice activity detection filtering.
            **kwargs: Additional arguments to pass to the model's transcribe method.

        Returns:
            str: The transcribed text.
        """
        segments, info = self.model.transcribe(
            audio_path,
            language=language,
            vad_filter=vad_filter,
            **kwargs
        )
        
        transcription = ""
        for segment in segments:
            transcription += segment.text + " "
        return transcription.strip()

if __name__ == "__main__":

    converter = SpeechToTextConverter(model_size="small", device="cpu") 

    try:
        transcribed_text = converter.transcribe_audio("test_audio.wav", language="en")
        print(f"Transcription: {transcribed_text}")
    except FileNotFoundError:
        print("Error: 'test_audio.wav' not found. Please create or provide a valid audio file.")
    except Exception as e:
        print(f"An error occurred during transcription: {e}")