"""Module containing text-to-speech code.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from enum import enum
import pyttsx3
from gtts import gTTS
from enum import enum
engine = pyttsx3.init()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)  # changes the voice
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

class Reader:
    """Reads aloud text according to the user's preferences.

    Attributes:
        voice: The voice engine used to speak words aloud.
    """

    class Voice(Enum):
        """Stores the list of voices the reader can use."""
        GOOGLE = 1
        PYTTSX = 2

    def __init__(self, voice):
        """Initializes Reader class"""
        if voice is not None:
            self.voice = Voice.GOOGLE

    def change_voice(self, voice):
        """Changes the reader's voice to the specified voice"""
        if voice = Voice.Google
