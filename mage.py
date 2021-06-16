#imports
import pygame
from Sprites.tower import Tower

#Mage
class Mage(pygame.sprite.Sprite):
    def __init__(self, spells):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\mage.png")
        self.rect = self.image.get_rect()
        self.spells = 5
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 1000
        self.repulsion = 0
        self.slowdown = 1
        fallen_enemies = 0
        screen = pygame.display.get_surface()
        self.rect.x = 0
        self.rect.y = 0
        self.attack = 5

#Functions
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
