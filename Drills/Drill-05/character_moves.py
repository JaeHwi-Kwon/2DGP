from pico2d import*
open_canvas()
grass=load_image('grass.png')
character=load_image('animation_sheet.png')

def set_initial_pos():
    return 203,535
def mov_character_by_route():
    pass


while True:
    x,y=set_initial_pos()
    mov_character_by_route()

close_canvas()