from pico2d import *

from Lecture15_Time import game_framework
import state_

PIXEL_PER_METER = (10.0 / 0.03)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class fly:
    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time

        if(bird.x>1600):
            bird.face_dir = -1
            bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time

        elif(bird.x < 0):
            bird.face_dir = 1
            bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(bird):
        if(bird.face_dir == -1):
            bird.image.clip_composite_draw(int(bird.frame) * 100, bird.action * 100, 100, 100, bird.x, bird.y)


class Bird:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.face_dir = 1
        self.image = load_image('bird_animation.png')

    def draw(self):
        self.draw()

    def update(self):
        pass