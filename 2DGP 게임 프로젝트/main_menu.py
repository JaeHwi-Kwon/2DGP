from pico2d import *
import game_framework
import Sound

BASED__MENU_X_POSITION = 1920/4
DELTA_OPAC = 0.8


class Menu:
    def __init__(self):
        self.image = [load_image('./Image/Title_Image/Title_%d.png' % i) for i in range(1, 7)]
        self.frame = 1
        self.x, self.y = 1920/2, 1080/2

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 6


class Select:
    def __init__(self):
        Sound.init()
        Sound.sets_sound_volume(Sound.sound_effect, 0, 128)
        self.pen_image = [load_image('./Image/Title_Image/Title_Pen_%d.png' % i) for i in range(1, 5)]
        self.select_image = [load_image('./Image/Title_Image/Title_Select_%d.png' % i) for i in range(1, 5)]
        self.frame = 0
        self.pen_x, self.pen_y = BASED__MENU_X_POSITION, 1080 / 3
        self.select_x, self.select_y = 1920/2, 1080/4
        self.selected = 1

    def draw(self):
        self.pen_image[int(self.frame)].draw(self.pen_x, self.pen_y)
        self.select_image[int(self.frame)].draw(self.select_x, self.select_y)

    def update(self):
        self.selected = clamp(1, self.selected, 3)
        self.pen_x = BASED__MENU_X_POSITION*self.selected
        self.frame = (self.frame + game_framework.frame_time*10) % 4


class Blackscreen:
    def __init__(self):
        self.image = load_image('./Image/Title_Image/black_screen.png')
        self.x, self.y = 1920/2, 1080/2
        self.opacity = 1.0

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.opacify(self.opacity)

    def update(self):
        if self.opacity:
            self.opacity -= game_framework.frame_time*DELTA_OPAC
        self.opacity = clamp(0.0, self.opacity, 1.0)
