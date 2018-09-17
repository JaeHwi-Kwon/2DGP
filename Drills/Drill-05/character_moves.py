from pico2d import*
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def mov_character(x, y, desx, desy):

    def mov_left(x, y, desx, desy):
        pass
    def mov_right(x, y, desx, desy):
        pass
    def mov_up(x, y, desx,desy):
        pass
    def mov_down(x, y, desx, desy):
        pass


def mov_character_by_route():

    def mov_character_from_to(x, y, desx, desy):

        def set_anime_destination(x, y, desx, desy):
            if x < desx:
                return 'right'
            elif x > desx:
                return 'left'

        destination = set_anime_destination(x, y, desx, desy)
        mov_character(x, y, desx, desy)

    mov_character_from_to(203, 535, 132, 243)
    mov_character_from_to(132, 243, 535, 470)
    mov_character_from_to(535, 470, 477, 203)
    mov_character_from_to(477, 203, 715, 136)
    mov_character_from_to(715, 136, 316, 225)
    mov_character_from_to(316, 225, 510, 92)
    mov_character_from_to(510, 92, 692, 518)
    mov_character_from_to(692, 518, 682, 336)
    mov_character_from_to(682, 336, 712, 349)
    mov_character_from_to(712, 349, 203, 535)
    pass


while True:
    mov_character_by_route()

close_canvas()