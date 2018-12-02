from pico2d import *

class Background:
    image = None
    def __init__(self):
        self.image = load_image('./Image/main_stage/Background_white.png')
        self.x = 1920/2
        self.y = 1080/2

    def exit(self):
        del(self.image)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
    pass