import game_framework
from pico2d import *

import game_world


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# 100 pixel = 3 meter


class Ghost:

    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.image = load_image('animation_sheet_ghost.png')
        self.dir = dir
        self.frame = 0
        self.opacity = 0
        self.opac_toggle = 0.05
        if dir == 1:
            self.angle = 3.141592 / 2
        else:
            self.angle = -3.141592 / 2

    def update(self):
        self.opacity += self.opac_toggle
        if self.opacity > 1.0:
            self.opac_toggle = - self.opac_toggle
        elif self.opacity < 0.0:
            self.opac_toggle = - self.opac_toggle
        self.angle -= 3.141592 / 180 * self.dir
        self.y += 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if self.dir == 1:
            self.angle = clamp(0, self.angle, 3.141592/2)
        else:
            self.angle = clamp(-3.141592, self.angle, 0)
        pass

    def draw(self):
        self.image.opacify(self.opacity)
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, self.angle, '', self.x - 25,
                                           self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100, self.angle, '', self.x + 25,
                                           self.y - 25 , 100, 100)

    def exit(self):
        pass