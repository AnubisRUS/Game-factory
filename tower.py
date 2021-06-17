import pygame
from settings import *
from enemy import *
class Tower:
    def __init__(self, tower_health):
        self.health = tower_health # Жизни башни
        self.image = pygame.image.load(r"assets\images\tower.png")
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.rect.x = 0
        self.rect.y = 400
    def enemy_collid(self):#проверка насоприкосновение с врагом
        if self.rect.colliderect():
            self.health = self.health - 1
    def draw_tower(self, screen):#рисуем башню
        screen.blit(self.image, self.rect)