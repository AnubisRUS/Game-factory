import pygame
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, hp, speed, cost):
        super().__init__()
        self.hp = hp
        self.speed = speed
        self.cost = cost
        self.image = pygame.image.load(r"assets\images\enemy.png")
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x -= self.speed
