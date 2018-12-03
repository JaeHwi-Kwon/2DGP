from pico2d import *
import game_framework
import random
import Sound

LEFT, RIGHT = 0, 1


class Background:
    image = None

    def __init__(self):
        self.image = [load_image('./Image/main_stage/Background/background %d.png' % i) for i in range(1, 4)]
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.frame = 1

    def set_center_object(self, john):
        self.center_object = john
        pass

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)
        self.image[int(self.frame)].opacify(0.2)


    def update(self):
        self.window_left = clamp(0,
                                 int(self.center_object.x) - self.canvas_width//2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height//2,
                                   self.h - self.canvas_height)
        self.frame = (self.frame + game_framework.frame_time*5) % 3


class Block:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = [load_image('./Image/main_stage/Block/block %d.png' % i) for i in range(1, 5)]
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = random.randint(0, 3)
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.window_left, self.window_bottom = self.x-60, self.y-60

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def set_center_object(self, john):
        self.center_object = john

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            0, 0,
            self.w, self.h,
            self.real_x, self.window_bottom)
        pass

    def update(self):
        if self.center_object.x <= self.canvas_width/2:
            self.real_x = self.x - 60
        elif self.center_object.x >= self.canvas_width*3-self.canvas_width/2:
            self.real_x = self.x - 60 - self.canvas_width*2
        else:
            self.real_x = self.window_left - self.center_object.x + self.canvas_width//2 - 60
        self.window_left = clamp(self.x,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.frame = (self.frame + game_framework.frame_time * 10) % 4
        pass




class Enemy:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.velocity = 3
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.image = [load_image('./Image/main_stage/Enemy/monster %d.png' % i) for i in range(1, 9)]
        self.frame = random.randint(0, 7)
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.window_left, self.window_bottom = self.x - 60, self.y - 60

    def get_bb(self):
        return self.x - 55, self.y - 55, self.x + 55, self.y + 55

    def set_direction_opposite(self):
        self.velocity = -self.velocity

    def set_center_object(self, john):
        self.center_object = john

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            0, 0,
            self.w, self.h,
            self.real_x, self.window_bottom)
        pass

    def update(self):
        self.x += self.velocity
        if self.center_object.x <= self.canvas_width/2:
            self.real_x = self.x - 60
        elif self.center_object.x >= self.canvas_width*3-self.canvas_width/2:
            self.real_x = self.x - 60 - self.canvas_width*2
        else:
            self.real_x = self.window_left - self.center_object.x + self.canvas_width//2 - 60
        self.window_left = clamp(self.x,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.frame = (self.frame + game_framework.frame_time * 10) % 8
        pass


class Cannon:
    image = None

    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.image = [load_image('./Image/main_stage/Cannon/cannon %d.png' % i) for i in range(1, 9)]
        self.frame = random.randint(1, 4)
        self.dir = dir
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.window_left, self.window_bottom = self.x - 60, self.y - 60

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def set_center_object(self, john):
        self.center_object = john

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            0, 0,
            self.w, self.h,
            self.real_x, self.window_bottom)
        pass

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 4 + self.dir*4
        if self.center_object.x <= self.canvas_width/2:
            self.real_x = self.x - 60
        elif self.center_object.x >= self.canvas_width*3-self.canvas_width/2:
            self.real_x = self.x - 60 - self.canvas_width*2
        else:
            self.real_x = self.window_left - self.center_object.x + self.canvas_width//2 - 60
        self.window_left = clamp(self.x,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)


class Bullet:
    image = None

    def __init__(self, x, y, velocity):
        Sound.init()
        self.initx, self.inity = x, y
        self.x, self.y = x, y
        self.velocity = velocity
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.image = [load_image('./Image/main_stage/Cannon/Bullet/bullet %d.png' % i) for i in range(1, 5)]
        self.frame = 1
        self.opacity = 0
        self.timer = 7.0
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.window_left, self.window_bottom = self.x - 60, self.y - 60

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def set_center_object(self, john):
        self.center_object = john
        pass

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            0, 0,
            self.w, self.h,
            self.real_x, self.window_bottom)
        self.image[int(self.frame)].opacify(self.opacity)
        pass

    def update(self):
        if self.x <= -60 and self.velocity < 0 or self.x >= 1920*3 + 60 and self.velocity > 0:
            self.x = self.initx
            self.opacity = 0
            self.timer = 7.0
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.x += self.velocity
            self.opacity = 1
        self.frame = (self.frame + game_framework.frame_time * 10) % 4
        if self.center_object.x <= self.canvas_width / 2:
            self.real_x = self.x - 60
        elif self.center_object.x >= self.canvas_width * 3 - self.canvas_width / 2:
            self.real_x = self.x - 60 - self.canvas_width * 2
        else:
            self.real_x = self.window_left - self.center_object.x + self.canvas_width // 2 - 60
        self.window_left = clamp(self.x,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)


class Trap:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.image = [load_image('./Image/main_stage/Trap/trap %d.png' % i) for i in range(1, 5)]
        self.frame = 1
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.window_left, self.window_bottom = self.x - 60, self.y - 60

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def set_center_object(self, john):
        self.center_object = john

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            0, 0,
            self.w, self.h,
            self.real_x, self.window_bottom)
        pass

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 4
        if self.center_object.x <= self.canvas_width/2:
            self.real_x = self.x - 60
        elif self.center_object.x >= self.canvas_width*3-self.canvas_width/2:
            self.real_x = self.x - 60 - self.canvas_width*2
        else:
            self.real_x = self.window_left - self.center_object.x + self.canvas_width//2 - 60
        self.window_left = clamp(self.x,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)


class Goal:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.image = [load_image('./Image/main_stage/Goal/clock %d.png' % i) for i in range(1, 7)]
        self.frame = 1
        self.w = self.image[0].w
        self.h = self.image[0].h
        self.window_left, self.window_bottom = self.x - 60, self.y - 60

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def set_center_object(self, john):
        self.center_object = john

    def draw(self):
        self.image[int(self.frame)].clip_draw_to_origin(
            0, 0,
            self.w, self.h,
            self.real_x, self.window_bottom)
        pass

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 6
        if self.center_object.x <= self.canvas_width/2:
            self.real_x = self.x - 60
        elif self.center_object.x >= self.canvas_width*3-self.canvas_width/2:
            self.real_x = self.x - 60 - self.canvas_width*2
        else:
            self.real_x = self.window_left - self.center_object.x + self.canvas_width//2 - 60
        self.window_left = clamp(self.x,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        pass
