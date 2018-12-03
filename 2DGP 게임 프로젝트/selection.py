from pico2d import *
selection = 1

def get_selection():
    global selection
    return selection

def selection_increase():
    global selection
    selection = selection + 1
    selection = clamp(1, selection, 4)

def selection_decrease():
    global selection
    selection = selection - 1
    selection = clamp(1, selection, 4)