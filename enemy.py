import pygame
from settings import *
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, hp, x, cost):
        super().__init__()
        self.hp = hp
        self.minspeed = 1
        self.maxspeed = 3
        self.speed = random.randrange(self.minspeed, self.maxspeed)
        self.cost = cost
        self.image = pygame.image.load(r"assets/design/skelet-01.jpeg")
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.rect.x = x
        self.rect.y = 515
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x -= self.speed