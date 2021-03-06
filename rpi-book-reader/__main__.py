"""Module defining code to setup the book reader's GUI.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

#from camera import *
from configparser import ConfigParser
#from motor import *
from pathlib import Path
from reader import *

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("__main__.kv")

class RPIBookReader(App, TabbedPanel):

    def build(self):
        config = ConfigParser()
        config.read(Path(__file__).parent /  "config.ini")

        #self.motor = Motor([10, 25, 8, 7])
        #self.camera = Camera()

        path_to_tesseract_exe = config.get('TesseractSettings', 'PathToTesseractEXE')
        if (path_to_tesseract_exe is not None):
            self.reader = Reader(path_to_tesseract_exe)
        else:
            self.reader = Reader()

        return self

class ImageButton(ButtonBehavior, Image):
    """Represents an Image that behaves like a button."""

class ToggleButtonImage(ToggleButtonBehavior, Image):
    """Represents an Image that behaves like a toggle button."""

    def toggle_state(self, widget, value):
        """Toggles the play/pause button"""
        app = App.get_running_app()
        if (value == "down"):
            self.source = "./icons/pause-button.png"
            app.reader.play()
            #app.motor.move()
        else:
            self.source = "./icons/play-button.png"
            app.reader.pause()

if __name__ == "__main__":
    app = RPIBookReader()
    app.run()
