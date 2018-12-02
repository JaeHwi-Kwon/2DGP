from pico2d import *
import game_framework
import Sound

BASED__MENU_X_POSITION = 1920/4
DELTA_OPAC = 0.8


class Menu:
    def __init__(self):
        self.image = [load_image('./Image/Title_Image/Title_%d.png' % i) for i in range(1, 6)]
        self.frame = 1
        self.x, self.y = 1920/2, 1080/2

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 5


class Select:
    def __init__(self):
        Sound.init()
        Sound.sets_sound_volume(Sound.sound_effect, 0, 128)
        self.pen_image = [load_image('./Image/Title_Image/Title_Pen_%d.png' % i) for i in range(1, 4)]
        self.select_image = [load_image('./Image/Title_Image/Title_Select_%d.png' % i) for i in range(1, 4)]
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
        self.frame = (self.frame + game_framework.frame_time*10) % 3

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                Sound.play_sound_effect(0)
                self.selected -= 1
            elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                Sound.play_sound_effect(0)
                self.selected += 1
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
                Sound.play_sound_effect(0)
                if self.selected == PLAY:
                    game_framework.push_state(world_build_state)
                elif self.selected == LOAD:
                    game_framework.push_state(select_state)
                elif self.selected == QUIT:
                    game_framework.quit()


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
