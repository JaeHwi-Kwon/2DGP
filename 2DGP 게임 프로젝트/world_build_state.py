import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

from John import John
from load_map import Block
from load_map import Enemy
from load_map import Cannon
from load_map import Goal
from load_map import Trap

john = None
block = None
enemy = None
cannon = None
goal = None
trap = None

BLANK, BLOCK, ENEMY, CANNON, TRAP, GOAL = range(6)

name = "WorldBuildState"

menu = None

def enter():
    pass

def pause():
    pass

def resume():
    pass

def create_new_world():
    global john
    john = John()
    game_world.add_object(john, 1)

    with open('first_stage_data.json', 'r') as f:
        stage_data_list = json.load(f)

    for i in stage_data_list:
        for j in stage_data_list[i]:
            if stage_data_list[i][j] == BLOCK:
                block = Block(60 + 120*j, 1020 - 120*i)
                game_world.add_object(block, 1)
                pass
            elif stage_data_list[i][j] == CANNON:
                cannon = Cannon(60 + 120 * j, 1020 - 120 * i)
                game_world.add_object(cannon, 1)
                pass
            elif stage_data_list[i][j] == ENEMY:
                enemy = Enemy(60 + 120 * j, 1020 - 120 * i)
                game_world.add_object(enemy, 2)
                pass
            elif stage_data_list[i][j] == TRAP:
                trap = Trap(60 + 120 * j, 1020 - 120 * i)
                game_world.add_object(trap, 2)
                pass
            elif stage_data_list[i][j] == GOAL:
                goal = Goal(60 + 120 * j, 1020 - 120 * i)
                game_world.add_object(goal, 3)
                pass


def load_saved_world():
    pass


def handle_events():
    pass


def update():
    pass


def draw():
    clear_canvas()

    update_canvas()
