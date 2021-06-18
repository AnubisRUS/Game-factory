#imports
import pygame
from tower import *
from enemy import *
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
        self.last_shot = pygame.time.get_ticks()

#Functions
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        if key[pygame.K_SPACE]:
            if key[pygame.K_SPACE] and now - self.last_shot > self.cooldown:
                enemy.health -= self.attack
                enemy.rect.x -= self.repulsion
                self.last_shot = now

    def level_up(self):
        self.attack += 2.5
        self.cooldown -= 25
        self.repulsion += 0.25

