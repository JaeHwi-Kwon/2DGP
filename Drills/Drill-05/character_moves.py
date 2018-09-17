from pico2d import*
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def mov_character(x, y, desx, desy):

    def mov_left(x):
        return x - 1
    def mov_right(x):
        pass
    def mov_up(y):
        pass
    def mov_down(y):
        pass

    frame = 0
    destination = 0
    while x != desx or y != desy:
        if x > desx:
            x = mov_left(x)
            destination = 0
        elif x < desx:
            x = mov_right(x)
            destination = 100

        if y > desy:
            y = mov_down(y)
        elif y < desy:
            y = mov_up(y)
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,destination,100,100,x,y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.02)
        get_events()


def mov_character_by_route():

    def mov_character_from_to(x, y, desx, desy):
        mov_character(x, y, desx, desy)

    mov_character_from_to(203, 535, 132, 243)
    #mov_character_from_to(132, 243, 535, 470)
    #mov_character_from_to(535, 470, 477, 203)
    #mov_character_from_to(477, 203, 715, 136)
    #mov_character_from_to(715, 136, 316, 225)
    #mov_character_from_to(316, 225, 510, 92)
    #mov_character_from_to(510, 92, 692, 518)
    #mov_character_from_to(692, 518, 682, 336)
    #mov_character_from_to(682, 336, 712, 349)
    #mov_character_from_to(712, 349, 203, 535)
    pass


while True:
    mov_character_by_route()

close_canvas()