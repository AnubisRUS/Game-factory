import pygame
from settings import *
from enemy import *
class Tower(pygame.sprite.Sprite):
    def __init__(self, tower_health):
        super().__init__()
        self.health = tower_health # Жизни башни
        self.image = pygame.image.load("assets/design/dogeburger.png")
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.rect.x = 48
        self.rect.y = 277
    def draw_tower(self, screen):#рисуем башню
        screen.blit(self.image, self.rect)
    def update(self):
        pass