#imports
import pygame
from Sprites.tower import Tower
from Sprites.enemy import Monster

#Mage
class Mage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets\Images\Mage.png")
        self.rect = self.image.get_rect()
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = mage_cooldown
        self.spells = mage_spells
        self.repulsion = mage_repulsion
        fallen_enemies = 0
        screen = pygame.display.get_surface()
        self.rect.x = 0
        self.rect.y = 0
        self.attack = mage_attack

#Functions
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

    def attack(self):
        enemy = Monster()
