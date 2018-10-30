import game_framework
from pico2d import *

import game_world


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Ghost:

    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.image = load_image('animation_sheet_ghost.png')
        self.dir = dir
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25
                                          , 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25
                                          ,100, 100)
        pass
