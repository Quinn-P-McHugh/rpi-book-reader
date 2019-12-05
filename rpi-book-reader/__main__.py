"""Module defining code to setup the book reader's GUI.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

#from camera import *
from configparser import ConfigParser
#from motor import *
from reader import *
import os

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
        parser = ConfigParser()
        parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

        #self.motor = Motor(15, 16, (17, 18, 19)) # Change these pins
        #self.camera = Camera()
        self.reader = Reader(parser.get('TesseractSettings', 'PathToTesseractEXE'))
        
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
        else:
            self.source = "./icons/play-button.png"
            app.reader.pause()

if __name__ == "__main__":
    app = RPIBookReader()
    app.run()
