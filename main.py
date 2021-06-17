# -*- coding: utf-8 -*- # строка нужна, чтобы не было ошибки Non-UTF-8 code starting with '\xd1' in file
import pygame
import pygame, sys, time
from settings import *
#import sprites
from buttons import *
from mage import *
from tower import *

pygame.init()

#creating window
screen = pygame.display.set_mode((width_window, height_window))
clock = pygame.time.Clock()


#show menu func
def mainmenu():
    #fonts
    arial = pygame.font.SysFont("Arial", 72)

    #sprites
    game_caption = arial.render("Fall of Darkness", True, (255, 255, 255))
    playbutton = Button((396, 98), "", (402, 281))
    tutorialbutton = Button((396, 98), "", (402, 443))
    exitbutton = Button((238, 81), "", (922, 580))

    running = True
    while running:

        clock.tick(FPS)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    startgame()
                if tutorialbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    tutorial()
                if exitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        #rendering
        screen.blit(game_caption, (410, 95))
        playbutton.draw(screen)
        tutorialbutton.draw(screen)
        exitbutton.draw(screen)

        #updates
        pygame.display.update()



#start game func
def startgame():
    # fonts
    arial = pygame.font.SysFont("Arial", 72)
    tower = Tower(tower_health)
    player = Mage(5)

    #sprites
    test_text = arial.render("GameFactory", True, (255, 255, 255))
    history_text_1p = arial.render("Вы волшебник, что пошëл по пути глубокого изучения магии. Из за ваших открытий вас все почетают, но вы настолько углубились в познание чудес магии, что отстроили свою башню на краю континента в глуши. ", True, (255, 255, 255))
    history_text_2p = arial.render("Однажды утром вы проснулись, заметив скопление маны в одной точке. Это был портал, который вëл в царство тьмы, где живут множество монстров. От туда полезли орды монстров, и все они устремились на вашу башню. ", True, (255, 255, 255))
    history_text_3p = arial.render("Вы готовы отбиваться от монстров, ведь вы чувствуете, что разгадка тайн магии уже близко. Но вас беспокоит чувство тревоги,  которое исходит из портала. Нет сомнений: там живëт что-то злобное и сильное.", True, (255, 255, 255))
    running = True
    screen.fill((0, 0, 0))
    screen.blit(test_text, (410, 300))
    pygame.display.update()
    time.sleep(5)
    screen.blit(history_text_1p, ())
    pygame.display.update()
    time.sleep(10)
    screen.blit(history_text_2p, ())
    pygame.display.update()
    time.sleep(10)
    screen.blit(history_text_3p, ())
    pygame.display.update()
    time.sleep(10)
    while running:
        clock.tick(FPS)
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # updates
        screen.fill((0, 0, 0))
        pygame.display.update()

def tutorial():
    # fonts
    arial = pygame.font.SysFont("Arial", 72)
    backbutton = Button((238, 81), "", (922, 580))
    #sprites
    tutorial_text = arial.render("Рады приветствовать вас в нашей игре fall of darkness.Цель игры - защита башни от наступающих монстров, для этого надо нажимать на (подставить кнопку), но у атаки есть откат. Убивая монстров вы получаете монеты, которые можно потратить на улучшения. Но монстры также будут повышать уровень, а через какое-то количество волн появится босс. Желаем приятно провести время в игре. ", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(tutorial_text, (10, 100))
    backbutton.draw(screen)
    running = True
    while running:

        clock.tick(FPS)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    mainmenu()

        # update
        pygame.display.update()



#showing menu
mainmenu()
