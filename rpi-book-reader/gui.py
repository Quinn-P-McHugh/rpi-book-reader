"""Module defining code to setup the book reader's GUI.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("gui.kv")

paused = True   # Whether or not the book reader is currently paused.

class GUI(App, TabbedPanel):
    paused = True

    def build(self):
        return self

    def get_paused(self):

        return paused

class ImageButton(ButtonBehavior, Image):
    """Represents an Image that behaves like a button."""
    def toggle_state(self):
        """Toggles the play/pause button"""
        app = App.get_running_app()
        if (app.paused == True):
            self.source = "./icons/pause-button.png"
        else:
            self.source = "./icons/play-button.png"
        app.paused = not app.paused

gui = GUI()
gui.run()
