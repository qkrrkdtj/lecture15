from pico2d import *
import game_framework

import game_world
from Lecture15_Time.bird import Bird
from grass import Grass
from boy import Boy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global bird

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    bird1 = Bird(100, 150)
    game_world.add_object(bird1, 1)

    bird2 = Bird(200, 150)
    game_world.add_object(bird2, 1)

    bird3 = Bird(300, 150)
    game_world.add_object(bird3, 1)

    bird4 = Bird(400, 150)
    game_world.add_object(bird4, 1)

    bird5 = Bird(500, 150)
    game_world.add_object(bird5, 1)

    bird6 = Bird(600, 150)
    game_world.add_object(bird6, 1)

    bird7 = Bird(700, 150)
    game_world.add_object(bird7, 1)

    bird8 = Bird(800, 150)
    game_world.add_object(bird8, 1)

    bird9 = Bird(900, 150)
    game_world.add_object(bird9, 1)

    bird10 = Bird(1000, 150)
    game_world.add_object(bird10, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

