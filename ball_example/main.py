# coding: utf-8

import sys
import pygame
import random
import numpy as np
from pygame.locals import *
from libs import ball as ba
from libs import agent as ag

pygame.init()
pygame.mixer.init()
sound_base_path = '/Users/joseph/work/CoopGame/ball_example'
pygame.mixer.music.load(sound_base_path + '/sounds/Symbiose.mp3')
pygame.mixer.music.play(-1)

WINDOWWIDTH = 640 * 2
WINDOWHEIGHT = 480 * 2

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ball survival !')

# frames per second setting
FPS = 50
fpsClock = pygame.time.Clock()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF.fill(BLACK)
N_BALLS = 5


agent = ag.Agent(**{
    'name': 'agent',
    'size': (30, 30),
    'pos': (random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT)),
})

ball_list = []
for k in range(N_BALLS):
    # ball instance
    settings = {
        'name': 'ball_' + str(k),
        'ref_sprite': 'orange',
        'size': (30, 30),
        'pos': (random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT)),
        'speed': (10 + random.randint(-5, 5), 10 + random.randint(-5, 5)),
        'screen': {'width': WINDOWWIDTH, 'height': WINDOWHEIGHT}
    }
    ball_list.append(ba.Ball(**settings))

all_balls_group = pygame.sprite.Group(ball_list)

for ball in ball_list:
    ball_group = pygame.sprite.Group(ball_list)
    ball_group.remove(ball)
    ball.other_balls_group = ball_group

counter = 0
while True:  # main loop
    # pygame.event.pump()
    counter += 1
    print('FRAME {}').format(counter)
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()

    DISPLAYSURF.fill(BLACK)

    # agent.search_new_pos(all_balls_group, 2)

    for ball in ball_list:
        ball.checkWallCollision(WINDOWWIDTH, WINDOWHEIGHT)

        ball_colliding = pygame.sprite.spritecollideany(ball, ball.other_balls_group)
        if ball_colliding:
            print('ball {} is colliding with ball {}').format(ball.name, ball_colliding.name)
            ball.collide_another_ball(ball_colliding)
            ball.flip_color()

    for ball in ball_list:
        ball.move()
        DISPLAYSURF.blit(ball.sprite, ball.pos)

    DISPLAYSURF.blit(agent.sprite, agent.pos)

    pygame.display.update()
    fpsClock.tick(FPS)
