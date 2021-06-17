# -*- coding: utf-8 -*- # строка нужна, чтобы не было ошибки Non-UTF-8 code starting with '\xd1' in file
import pygame
import pygame, sys, time
from settings import *
#import sprites
from Sprites.buttons import *
from Sprites.mage import *
from Sprites.tower import *
from Sprites.enemy import *

pygame.init()
pygame.mixer.init()

#Stuff
Monsters = pygame.sprite.Group()

#creating window
screen = pygame.display.set_mode((width_window, height_window))
clock = pygame.time.Clock()

pygame.mixer.music.load('assets/sounds/162385647786772.mp3')
pygame.mixer.music.play(10)
#show menu func
def mainmenu():
    #fonts
    fnpx = pygame.font.Font("assets/fonts/ancient-modern-tales-font/AncientModernTales-a7Po.ttf", 82)

    #sprites
    game_caption = fnpx.render("Fall of Darkness", True, (255, 255, 255))
    playbutton = Button(r"assets/design/playbutton.png", (735, 281))
    tutorialbutton = Button(r"assets/design/tutorialbutton.png", (735, 443))
    exitbutton = Button(r"assets/design/exitbutton.png", (735, 580))

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
        screen.blit(game_caption, (700, 95))
        playbutton.draw(screen)
        tutorialbutton.draw(screen)
        exitbutton.draw(screen)

        #updates
        pygame.display.update()



#start game func
def startgame():
    # fonts
    fnpx = pygame.font.Font("assets/fonts/CyrillicPixel7-LPeg.ttf", 35)
    player = Mage(5)
    tower = Tower(tower_health)


    #sprites
    test_text = fnpx.render("GameFactory", True, (255, 255, 255))
    history_text_1p = fnpx.render("Вы волшебник, что пошëл по пути глубокого изучения магии. Из за ваших открытий вас все почетают, но вы настолько углубились в познание чудес магии, что отстроили свою башню на краю континента в глуши. ", True, (255, 255, 255))
    history_text_2p = fnpx.render("Однажды утром вы проснулись, заметив скопление маны в одной точке. Это был портал, который вëл в царство тьмы, где живут множество монстров. От туда полезли орды монстров, и все они устремились на вашу башню. ", True, (255, 255, 255))
    history_text_3p = fnpx.render("Вы готовы отбиваться от монстров, ведь вы чувствуете, что разгадка тайн магии уже близко. Но вас беспокоит чувство тревоги,  которое исходит из портала. Нет сомнений: там живëт что-то злобное и сильное.", True, (255, 255, 255))
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
    fnpx = pygame.font.Font("assets/fonts/CyrillicPixel7-LPeg.ttf", 35)
    backbutton = Button(r"assets/design/backbutton.png", (760, 580))
    #sprites
    tutorial_text1 = fnpx.render("Рады приветствовать вас в нашей игре fall of darkness.", True, (255, 255, 255))
    tutorial_text2 = fnpx.render("Цель игры - защита башни от наступающих монстров,  ", True, (255, 255, 255))
    tutorial_text3 = fnpx.render("для этого надо нажимать на пробел, но у атаки есть откат.  ", True,(255, 255, 255))
    tutorial_text4 = fnpx.render("Убивая монстров вы получаете монеты, которые можно", True,(255, 255, 255))
    tutorial_text5 = fnpx.render("потратить на улучшения. Но монстры также будут", True,(255, 255, 255))
    tutorial_text6 = fnpx.render("повышать уровень, а через какое-то ", True,(255, 255, 255))
    tutorial_text7 = fnpx.render("количество волн появится босс", True,(255, 255, 255))
    tutorial_text8 = fnpx.render("Желаем приятно провести время в игре.", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(tutorial_text1, (20, 280))
    screen.blit(tutorial_text2, (20, 330))
    screen.blit(tutorial_text3, (20, 380))
    screen.blit(tutorial_text4, (20, 430))
    screen.blit(tutorial_text5, (20, 480))
    screen.blit(tutorial_text6, (20, 530))
    screen.blit(tutorial_text7, (20, 580))
    screen.blit(tutorial_text8, (20, 630))

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
