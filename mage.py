#imports
import pygame
from tower import *

#Mage
class Mage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/design/mage.png")
        self.rect = self.image.get_rect()
        self.spells = 5
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 1000
        self.repulsion = 0
        self.slowdown = 1
        fallen_enemies = 0
        screen = pygame.display.get_surface()
        self.rect.x = 127
        self.rect.y = 173
        self.attack = 5

#Functions
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

    def level_up(self):
        self.attack += 2.5
        self.cooldown -= 25
        self.repulsion += 0.25