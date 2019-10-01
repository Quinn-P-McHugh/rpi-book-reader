"""Module defining code to setup the book reader's GUI.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

Builder.load_string("""
<GUI>:
    ImageButton:
        source: './images/play-button.png'
        size_hint: .2, .2
""")

paused = True   // Whether or not the book reader is currently paused.

class GUI(App, AnchorLayout):
    def build(self):
        return self

class ImageButton(ButtonBehavior, Image):
    """Represents an image with button functionality.

    Attributes:
        ButtonBehavior: Mixin class that provides Button behavior
        Image: Image class
    """
    def on_press(self):
        global paused
        if (paused == True):
            self.source = "./images/pause-button.png"
        else:
            self.source = "./images/play-button.png"
        paused = not paused

GUI().run()
