import speech_recognition as sr
from ..util import config
# import os
import logging

logger = logging.getLogger(__name__)


class SpeechToTextConverter:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # self.pathes = self.read_file_paths(config.FILES_PATH)

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
                logger.info(f"audio file converted to text.")
                return text
        except sr.UnknownValueError:
            logger.error("Google Speech Recognition could not understand audio.")
            return None
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except FileNotFoundError:
            logger.error(f"Audio file not found at: {audio_file_path}")
            return None

#     @staticmethod
#     def read_file_paths(directory:str)->list[str]:
#         """
#         a method that returns all the file pathes in a directory

#         Args:

#             directory path str.
#         Returns:
        
#                 all the files pathes in the directory.
#         """
#         return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

#  if __name__ == "__main__":
#     converter = SpeechToTextConverter()
#     path = converter.pathes[5]
#     x = converter.transcribe_audio_file(path)
#     if x:
#         print(f"converted data {x}")

      

