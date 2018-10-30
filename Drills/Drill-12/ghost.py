import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3)
ANGLE_PER_SECOND = (3.141592*2)*2
FRAME_PER_SECOND = 60
ANGLE_PER_FRAME = ANGLE_PER_SECOND/FRAME_PER_SECOND

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Ghost:

    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.image = load_image('animation_sheet_ghost.png')
        self.dir = dir
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.opacity = 0
        self.opac_toggle = 0.05
        self.circ_toggle = False
        self.circ_angle = 3.141592/180*270
        self.cirx, self.ciry = x, y + 270
        if dir == 1:
            self.angle = 3.141592 / 2
        else:
            self.angle = -3.141592 / 2

    def update(self):
        # opacity
        self.opacity += self.opac_toggle
        if self.opacity > 1.0:
            self.opac_toggle = - self.opac_toggle
        elif self.opacity < 0.0:
            self.opac_toggle = - self.opac_toggle

        # frame
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        # translate
        if self.angle > 0 and self.dir == 1:
            self.y += 2
        elif self.angle < 0 and self.dir == -1:
            self.y += 2

        # rotate
        self.angle -= 3.141592 / 180 * self.dir
        if self.dir == 1:
            self.angle = clamp(0, self.angle, 3.141592/2)
        else:
            self.angle = clamp(-3.141592, self.angle, 0)

        if self.y == 270:
            self.circ_toggle = True

        if self.circ_toggle:
            self.circ_angle += ANGLE_PER_FRAME
            self.x = self.cirx + PIXEL_PER_METER*3*math.cos(self.circ_angle)
            self.y = self.ciry + PIXEL_PER_METER*3*math.sin(self.circ_angle)

    def draw(self):
        self.image.opacify(self.opacity)
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, self.angle, '', self.x - 25,
                                           self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100, self.angle, '', self.x + 25,
                                           self.y - 25, 100, 100)

    def exit(self):
        pass
