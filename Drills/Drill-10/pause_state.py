import game_framework
from pico2d import *

name = 'PauseState'
image = None

pause = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400,300)