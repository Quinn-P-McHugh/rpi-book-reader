"""Module startup code for Raspberry Pi book reader.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from camera import *
from gui import *

camera = Camera()
gui = GUI()
gui.run()

import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()
