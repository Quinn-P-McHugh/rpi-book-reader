"""Module startup code for Raspberry Pi book reader.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from camera import *
from gui import *
from motor import *

motor = Motor(15, 16, (17, 18, 19)) # Change these pins
camera = Camera()
gui = GUI()
gui.run()

import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()
