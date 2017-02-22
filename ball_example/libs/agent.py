# coding: utf-8

import pygame

class Agent(pygame.sprite.Sprite):
    """Agent creator """
    def __init__(self, name, size, pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load('./images/yellowball.png')
        self.size = size
        self.sprite = pygame.transform.scale(self.image, self.size)
        self.pos = pos

    def search_new_pos(self, ball_group, depth):
        pos_speed_list = [{'pos': x.pos, 'speed': x.speed} for x in ball_group]
        next_pos_speed = estimate_next_pos_speed(pos_speed_list)
        print(next_pos_speed)
        return next_pos_speed


def compute_next_pos_speed(elem):
    return {
        'pos': tuple([r + v for r, v in zip(elem.pos, elem.speed)]),
        'speed': elem.speed
    }


def estimate_next_pos_speed(pos_speed_list):
    return map(pos_speed_list, compute_next_pos_speed)


def evaluate_situation(ref_pos, list_other_pos):
    value = sum(map(list_other_pos,
                    lambda x: abs(ref_pos[0]-x[0]) + abs(ref_pos[1]-x[1])
                    )
                )
    return value
