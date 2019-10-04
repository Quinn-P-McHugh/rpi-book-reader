"""Module defining code to setup the camera.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

import datetime
from time import strftime
#from picamera import PiCamera

class Camera:
    #def __init__(self):
        
    def take_picture(self):
        time = datetime.datetime.now().isoformat()
        self.capture("./images/" + time + ".jpg")
