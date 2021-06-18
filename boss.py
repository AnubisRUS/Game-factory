import pygame
from enemy import Monster
from settings import *
class Boss(Monster):
    def __init__(self, x):
        super().__init__()
        self.hp = boss_hp
        self.cost = boss_cost