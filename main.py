from pico2d import *
from boy import Boy
from grass import Grass
from grass import Grass2
from ball import Ball
import game_world


# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

def reset_world():
    global boy

    grass1 = Grass()
    game_world.add_objects([grass1], 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    grass2 = Grass2()
    game_world.add_objects([grass2], 1)

def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
