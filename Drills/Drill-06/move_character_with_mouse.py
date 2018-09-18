from pico2d import*

KPU_WIDTH, KPU_HEIGHT = 1280,1024

def move_character(x,y,characterx,charactery):
    while character != x and character != y:
        if characterx < x:
            characterx += 1
        elif character > x:
            characterx -= 1
        if charactery < y:
            charactery += 1
        elif charactery > y:
            charactery -= 1

def handle_events():
    global running
    global x,y
    global dir
    global characterx,charactery
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONUP and event.key == SDL_BUTTON_LEFT:
            x,y = event.x, KPU_HEIGHT - 1 - event.y
            move_character(x,y,characterx,charactery)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x,y = KPU_WIDTH//2, KPU_HEIGHT//2
characterx, charactery = KPU_WIDTH//2, KPU_HEIGHT//2
frame = 0
dir = 0
hide_cursor()
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH //2, KPU_HEIGHT //2)
    character.clip_draw(frame*100,100*dir,100,100,characterx,charactery)
    cursor.draw(x, y)
    update_canvas()
    frame = (frame+1) % 8

    delay(0.02)
    handle_events()

close_canvas()