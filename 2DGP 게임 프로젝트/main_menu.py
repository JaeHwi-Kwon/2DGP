from pico2d import *
import game_framework
import Sound

BASED_MENU_X_POSITION_TRIO = 1920/4
BASED_MENU_X_POSITION_DUO = 1920/4
BASED_MENU_Y_POSITION = 1080/5*2
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
        self.pen_x, self.pen_y = BASED_MENU_X_POSITION_TRIO, 1080 / 3
        self.select_x, self.select_y = 1920/2, 1080/4
        self.selected = 1

    def draw(self):
        self.pen_image[int(self.frame)].draw(self.pen_x, self.pen_y)
        self.select_image[int(self.frame)].draw(self.select_x, self.select_y)

    def update(self):
        self.selected = clamp(1, self.selected, 3)
        self.pen_x = BASED_MENU_X_POSITION_TRIO*self.selected
        self.frame = (self.frame + game_framework.frame_time*10) % 4


class Stage_Select:
    def __init__(self):
        Sound.init()
        Sound.sets_sound_volume(Sound.sound_effect, 0, 128)
        self.pen_image = [load_image('./Image/Title_Image/Title_Pen_%d.png' % i) for i in range(1, 5)]
        self.frame = 0
        self.pen_x, self.pen_y = BASED_MENU_X_POSITION_DUO, BASED_MENU_Y_POSITION
        self.selected = 0

    def draw(self):
        self.pen_image[int(self.frame)].draw(self.pen_x, self.pen_y)

    def update(self):
        self.selected = clamp(0, self.selected, 3)
        self.pen_x = BASED_MENU_X_POSITION_DUO*(2*(self.selected % 2) + 1)
        self.pen_y = BASED_MENU_Y_POSITION*(2 - self.selected // 2)
        self.frame = (self.frame + game_framework.frame_time*10) % 4

class Stage_Select_Back:
    def __init__(self):
        self.image = [load_image('./Image/Title_Image/Select %d.png' % i) for i in range(1,4)]
        self.frame = 0
        self.x = get_canvas_width()/2
        self.y = get_canvas_height()/2

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 3

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


class Whitescreen:
    def __init__(self):
        self.image = load_image('./Image/Title_Image/white_screen.png')
        self.x, self.y = 1920/2, 1080/2

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

