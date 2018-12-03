import random
import json
import os

from pico2d import *
import game_framework
import game_world
import Sound

import world_build_state
import select_state
import goal_state
import failure_state

name = "MainState"

black = None
john = None
blocks = []
enemies = []
cannons_l = []
cannons_r = []
goals = []
traps = []
bullets = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def collide_up(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if top_a >= bottom_b and a.y > a.y2:
        return True


def collide_down(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if bottom_a <= top_b and a.y <= a.y2:
        return True


def collide_left(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a <= right_b and a.x < a.x2:
        return True


def collide_right(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if right_a >= left_b and a.x > a.x2:
        return True

def collide_left_obj(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a <= right_b:
        return True


def collide_right_obj(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if right_a >= left_b:
        return True


def enter():
    global black
    black = load_image('./Image/main_stage/Background/background.png')
    global john, blocks, enemies, cannons_l, cannons_r, goals, traps, bullets
    john = world_build_state.get_john()
    blocks = game_world.objects[2]
    enemies = game_world.objects[3]
    cannons_l = game_world.objects[4]
    cannons_r = game_world.objects[5]
    bullets = game_world.objects[6]
    traps = game_world.objects[7]
    goals = game_world.objects[8]
    Sound.init()
    Sound.play_background_sound(0)


def exit():
    Sound.stop_background_sound(0)
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(select_state)
        else:
            john.handle_event(event)




def update():
    global john
    for game_object in game_world.all_objects():
        game_object.update()

        blocks = game_world.objects[2]
        enemies = game_world.objects[3]
        cannons_l = game_world.objects[4]
        cannons_r = game_world.objects[5]
        bullets = game_world.objects[6]
        traps = game_world.objects[7]
        goals = game_world.objects[8]

    for block in blocks:
        if collide(john, block):
            if collide_left(john, block) or collide_right(john, block):
                john.back_to_the_position_before_x()
            if collide_up(john, block) or collide_down(john, block):
                john.back_to_the_position_before_y()

    for enemy in enemies:
        if collide(john, enemy):
            game_framework.change_state(failure_state)
        for block in blocks:
            if collide(enemy, block):
                if collide_left_obj(enemy, block) or collide_right_obj(enemy, block):
                    enemy.set_direction_opposite()

    for trap in traps:
        if collide(john, trap):
            game_framework.change_state(failure_state)

    for cannon in cannons_l:
        if collide(john, cannon):
            if collide_left(john, cannon) or collide_right(john, cannon):
                john.back_to_the_position_before_x()
            if collide_up(john, cannon) or collide_down(john, cannon):
                john.back_to_the_position_before_y()

    for cannon in cannons_r:
        if collide(john, cannon):
            if collide_left(john, cannon) or collide_right(john, cannon):
                john.back_to_the_position_before_x()
            if collide_up(john, cannon) or collide_down(john, cannon):
                john.back_to_the_position_before_y()

    for bullet in bullets:
        if collide(john, bullet):
            game_framework.change_state(failure_state)

    for goal in goals:
        if collide(john, goal):
            game_framework.change_state(goal_state)

    if john.y <= 0:
        game_framework.change_state(failure_state)




def draw():
    clear_canvas()
    global black
    black.draw(1920 * 3 / 2, 1080 / 2)
    black.opacify(0.95)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







