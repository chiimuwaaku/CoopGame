# coding: utf-8

import pygame
import numpy as np

SPRITES = {
    'blue': './images/blueball.png',
    'orange': './images/orangeball.png'
}


class Ball(pygame.sprite.Sprite):
    """Ball creator """

    def __init__(self, name, ref_sprite, size, pos, speed, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.name = name
        self.ref_sprite = ref_sprite
        self.image = pygame.image.load(SPRITES[ref_sprite])
        self.size = size
        self.sprite = pygame.transform.scale(self.image, self.size)
        self.pos = pos
        self.speed = speed
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.sprite.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.other_balls_group = None
        self.screen = screen

    def bounce(self, direction):
        if direction == 'vertical':
            factor = [1, -1]
        elif direction == 'horizontal':
            factor = [-1, 1]
        self.speed = tuple([a*b for a, b in zip(self.speed, factor)])
        return self

    def next_pos(self):
        next_pos = tuple([item1 + item2 for item1, item2 in zip(self.pos, self.speed)])
        next_pos = (next_pos[0] % self.screen['width'], next_pos[1] % self.screen['height'])
        return next_pos

    def move(self):
        self.pos = self.next_pos()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        return self

    def checkWallCollision(self, window_width, window_height):
        next_pos = self.next_pos()
        if (next_pos[0] > (window_width - self.size[0]) or next_pos[0] < 0):
            self.bounce('horizontal')
        if (next_pos[1] > (window_height - self.size[1]) or next_pos[1] < 0):
            self.bounce('vertical')
        return self

    def collide_another_ball(self, other_ball):
        coords = relative_pos(self, other_ball)
        if coords[0] > 0 and coords[1] > 0:
            # cadrant de droite
            print('cadrant de droite :{}').format(coords)
            self.bounce('horizontal')
        elif coords[0] < 0 and coords[1] > 0:
            # cadrant inferieur
            print('cadrant inférieur :{}').format(coords)
            self.bounce('vertical')
        elif coords[0] < 0 and coords[1] < 0:
            # cadrant de gauche
            print('cadrant de gauche :{}').format(coords)
            self.bounce('horizontal')
        elif coords[0] > 0 and coords[1] < 0:
            # cadrant de superieur
            print('cadrant supérieur :{}').format(coords)
            self.bounce('vertical')
        else:
            print('else :{}').format(coords)

        return self

    def flip_color(self):
        if self.ref_sprite == 'blue':
            self.image = pygame.image.load(SPRITES['orange'])
            self.ref_sprite = 'orange'
        else:
            self.image = pygame.image.load(SPRITES['blue'])
            self.ref_sprite = 'blue'
        self.sprite = pygame.transform.scale(self.image, self.size)
        return self

    def get_center(self):
        center = {
            'x': None,
            'y': None
            }
        center['x'] = self.pos[0] + self.size[0] / 2.0
        center['y'] = self.pos[1] + self.size[1] / 2.0
        return center


def relative_pos(ref_ball, other_ball):
    e1 = np.array([1, 1])
    e2 = np.array([1, -1])
    relative_vec = np.array([0, 0])
    ref_center = ref_ball.get_center()
    other_center = other_ball.get_center()
    relative_vec[0] = other_center['x'] - ref_center['x']
    relative_vec[1] = other_center['y'] - ref_center['y']
    coord1 = np.dot(relative_vec, e1)
    coord2 = np.dot(relative_vec, e2)
    return (coord1, coord2)
