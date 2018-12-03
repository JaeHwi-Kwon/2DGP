from pico2d import *
background_sound, sound_effect = None, None


def init():
    global background_sound, sound_effect

    background_sound = [load_music('./Sound/night sound.wav'), load_music('./Sound/goal morning.wav'),
                        load_music('./Sound/main music.wav')]
    sound_effect = [load_wav('./Sound/menu select.wav'), load_wav('./Sound/john walking.wav'),
                    load_wav('./Sound/john jump.wav'), load_wav('./Sound/failure state.wav')]


def play_background_sound(number):
    background_sound[number].repeat_play()


def stop_background_sound(number):
    background_sound[number].stop()


def repeated_play_sound_effect(number):
    sound_effect[number].repeat_play()


def play_sound_effect(number):
    sound_effect[number].play()


def sets_sound_volume(sound_sort, number, volume):
    sound_sort[number].set_volume(volume)