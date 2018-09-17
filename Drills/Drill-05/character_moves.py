from pico2d import*
open_canvas()
grass=load_image('grass.png')
character=load_image('animation_sheet.png')

def set_initial_pos():
    return 203,535

def mov_character(x,y,desx,desy,des):

    def mov_left(x,y,desx,desy):
        pass
    def mov_right(x,y,desx,desy):
        pass

    if des=='left':
        mov_left(x,y,desx,desy)
    elif des=='right':
        mov_right(x,y,desx,desy)


def mov_character_by_route():

    def mov_character_from_to(x, y, desx, desy):

        def set_anime_destination(x, y, desx, desy):
            if x < desx:
                return 'right'
            elif x > desx:
                return 'left'

        destination = set_anime_destination(x, y, desx, desy)
        mov_character(x, y, desx, desy,destination)

    mov_character_from_to(x, y, 132, 243)
    mov_character_from_to(x, y, 535, 470)
    mov_character_from_to(x, y, 477, 203)
    mov_character_from_to(x, y, 715, 136)
    mov_character_from_to(x, y, 316, 225)
    mov_character_from_to(x, y, 510, 92)
    mov_character_from_to(x, y, 692, 518)
    mov_character_from_to(x, y, 682, 336)
    mov_character_from_to(x, y, 712, 349)
    mov_character_from_to(x, y, 203, 535)
    pass


while True:
    x,y=set_initial_pos()
    mov_character_by_route()

close_canvas()