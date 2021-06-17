import pygame
from settings import *

class Enemy:
    def __init__(self, hp, speed, cost):
        self.hp = hp
        self.speed = speed
        self.cost = cost
        self.image = pygame.image.load(r"assets\images\enemy.png")
        self.rect = self.image.get_rect()