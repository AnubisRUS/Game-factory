import pygame
from settings import *
from enemy import *
class Tower(pygame.sprite.Sprite):
    def __init__(self, tower_health):
        self.health = tower_health # Жизни башни
        self.image = pygame.Surface((52, 277))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.rect.x = 0
        self.rect.y = 400
    def enemy_collid(self):#проверка насоприкосновение с врагом
        if self.rect.colliderect():
            self.health = self.health - 1
    def draw_tower(self, screen):#рисуем башню
        screen.blit(self.image, self.rect)