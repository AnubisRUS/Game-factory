import pygame
from settings import *
from drawing import *
from tower import *
pygame.init()
sc = pygame.display.set_mode((width_window, height_window))#полотно размером с весь экран
drawing = Drawing(sc)#назначения класса для рисования
drawing.menu()#рисование меню