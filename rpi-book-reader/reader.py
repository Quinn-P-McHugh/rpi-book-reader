"""Module containing text-to-speech code.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from gtts import gTTS
from enum import Enum
import os
from PIL import Image
from playsound import playsound
from pytesseract import *

class Reader:
    """Reads aloud text from camera according to the user's preferences.

    Attributes:
        voice: The voice engine used to speak words aloud.
        paused: Whether or not the reader is paused.
    """

    class Voice(Enum):
        """Stores the list of voices the reader can use."""
        GOOGLE = 1
        PYTTSX = 2

    def __init__(self, pathToTesseractEXE=None, voice=None):
        """Initializes Reader class"""
        if voice is None:
            self.voice = Reader.Voice.GOOGLE
        else:
            self.voice = voice

        self.paused = True

        if pathToTesseractEXE is not None:
            pytesseract.tesseract_cmd = pathToTesseractEXE

    def change_voice(self, voice):
        """Changes the reader's voice to the specified voice"""
        try:
            self.voice = voice;
        except ValueError:
            raise Exception(voice + "is not a valid voice type." )

    def pause(self):
        """Pauses the reader"""
        self.paused = True

    def play(self):
        """Plays the reader."""
        self.paused = False

    def read_image(self, image_file):
        string = self.__image_to_string(image_file)
        self.__read(string)

    def __image_to_string(self, image_file):
        return pytesseract.image_to_string(Image.open(image_file))

    def __read(self, string):
        if (self.voice == Reader.Voice.GOOGLE):
            print ("reading")
            tts = gTTS(text='Good morning', lang='en')
            audio_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'audio', 'temp.mp3')
            tts.save(audio_file_path)
            playsound(audio_file_path)
