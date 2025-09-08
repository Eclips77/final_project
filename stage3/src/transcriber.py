import speech_recognition as sr
from ..utils import config

class SpeechToTextConverter:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio_file(self, audio_file_path):
        """
        Transcribes speech from an audio file.

        Args:
            audio_file_path (str): The path to the audio file (e.g., .wav).

        Returns:
            str: The transcribed text, or None if an error occurs.
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
                return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except FileNotFoundError:
            print(f"Audio file not found at: {audio_file_path}")
            return None



if __name__ == "__main__":
    converter = SpeechToTextConverter()
    for path in config.FILES_PATH:
        transcribed_text_file = converter.transcribe_audio_file(config.FILES_PATH)
        if transcribed_text_file:
            print(f"Transcribed from file: {transcribed_text_file}")
        break

