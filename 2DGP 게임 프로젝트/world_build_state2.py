import random
import json
import pickle
import os

from pico2d import *
import game_framework
import main_state
import game_world

import main_state

from John import John
from load_map import Block
from load_map import Enemy
from load_map import Cannon
from load_map import Goal
from load_map import Trap
from load_map import Background

black = None
back = None
john = None
block = None
enemy = None
cannon = None
goal = None
trap = None

blocks = []
enemies = []
cannons = []
traps = []
goals = []

BLANK, BLOCK, ENEMY, CANNON, TRAP, GOAL = range(6)
BLOCK_WIDTH = 120
BLOCK_HEIGHT = 120

name = "WorldBuildState"

menu = None



def enter():

    global back
    back = Background()
    game_world.add_object(back, 0)

    global john
    john = John()
    game_world.add_object(john, 1)

    back.set_center_object(john)
    john.set_background(back)

    with open('first_stage_data.json', 'r') as f:
        stage_data_list = json.load(f)

    for i in range(stage_data_list[0][0]):
        for j in range(stage_data_list[0][1]):
            if stage_data_list[1][i][j] == BLOCK:
                blocks.append([60 + 120 * j, 1020 - 120 * i])
                pass
            elif stage_data_list[1][i][j] == CANNON:
                cannons.append([60 + 120 * j, 1020 - 120 * i])
                pass
            elif stage_data_list[1][i][j] == ENEMY:
                enemies.append([60 + 120 * j, 1020 - 120 * i])
                pass
            elif stage_data_list[1][i][j] == TRAP:
                traps.append([60 + 120 * j, 1020 - 120 * i])
                pass
            elif stage_data_list[1][i][j] == GOAL:
                goals.append([60 + 120 * j, 1020 - 120 * i])
            else:
                pass
    global block
    block = [Block(blocks[i][0],blocks[i][1]) for i in range]
    game_world.add_object(block, 1)

    global cannon
    cannon = [Cannon(cannons[i][0].cannons[i][1]) for i in range]
    game_world.add_object(cannon, 1)

    global enemy
    enemy = [Enemy(enemies[i][0], enemies[i][1]) for i in range]
    game_world.add_object(enemy, 2)

    global trap
    trap = [Trap(traps[i][0], traps[i][1]) for i in range]
    game_world.add_object(trap, 2)

    global goal
    goal = [Goal(goals[i][0], goals[i][1]) for i in range]
    game_world.add_object(goal, 3)

    game_framework.change_state(main_state)
    
def exit():
    pass


def pause():
    pass


def resume():
    pass


def get_john():
    return john


def get_objects():
    return blocks, cannons, enemies, traps, goals

def get_world_size():
    with open('first_stage_data.json', 'r') as f:
        stage_data_list = json.load(f)
    return stage_data_list[0][0] * BLOCK_WIDTH, stage_data_list[0][1] * BLOCK_HEIGHT


def create_new_world():
    pass


def load_saved_world():
    pass


def handle_events():
    pass


def update():
    pass


def draw():
    pass
