# -*- coding: utf-8 -*- # строка нужна, чтобы не было ошибки Non-UTF-8 code starting with '\xd1' in file
import pygame
import pygame, sys, time
from settings import *
import random
#import sprites
from buttons import *
from mage import *
from tower import *
from enemy import *
from boss import *

pygame.init()
pygame.mixer.init()


#creating window
background = pygame.image.load("assets/design/menubg.png")
screen = pygame.display.set_mode((width_window, height_window))
clock = pygame.time.Clock()
pygame.display.set_caption("Fall of Darkness")
pygame.mixer.music.load('assets/sounds/162385647786772.mp3')
pygame.mixer.music.set_volume(voloume_music)
pygame.mixer.music.play(1000)
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
        screen.fill((0, 0, 0))
        screen.blit(game_caption, (700, 95))
        playbutton.draw(screen)
        tutorialbutton.draw(screen)
        exitbutton.draw(screen)

        #updates
        pygame.display.update()



#start game func
def startgame():
    # fonts
    #минимум монет с моба

    fnpx = pygame.font.Font("assets/fonts/CyrillicPixel7-LPeg.ttf", 25)
    player = Mage()
    tower = Tower(tower_health)
    Monsters = pygame.sprite.Group()

    #sprites
    history_text = [fnpx.render("Вы волшебник, что пошел по пути глубокого изучения магии. Из за ваших открытий вас", True, (255, 255, 255)), fnpx.render("все почетают, но вы настолько углубились в познание чудес магии,", True, (255, 255, 255)), fnpx.render("что отстроили свою башню на краю континента в глуши. ", True, (255, 255, 255)),\
                    fnpx.render("Однажды утром вы проснулись, заметив скопление маны в одной точке. Это был портал,", True, (255, 255, 255)), fnpx.render("который вeл в царство тьмы, где живут множество монстров.", True, (255, 255, 255)), fnpx.render("От туда полезли орды монстров, и все они устремились на вашу башню. ", True, (255, 255, 255)),
                    fnpx.render("Вы готовы отбиваться от монстров, ведь вы чувствуете, что разгадка тайн магии ", True, (255, 255, 255)), fnpx.render("уже близко.Но вас беспокоит чувство тревоги, которое исходит из портала. ", True, (255, 255, 255)), fnpx.render("Нет сомнений: там живет что-то злобное и сильное.", True, (255, 255, 255))]
    running = True
    story_mod = True
    nstory = 0
    x = 10
    y = 10
    screen.fill((0, 0, 0))
    for i in range(3):
        screen.blit(history_text[nstory], (x, y))
        nstory += 1
        y += 40
    pygame.display.update()
    while story_mod == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    if nstory <= 8:
                        for i in range(3):
                            screen.blit(history_text[nstory], (x, y))
                            pygame.display.update()
                            nstory += 1
                            y += 40
                    else:
                        story_mod = False

    while running and tower.health > 0:
        clock.tick(FPS)
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if len(Monsters) < 3:
            Monster1 = Monster(monster_hp, random.randrange(1300, 1900), random.randrange(mminmon, mmaxmon))
            Monsters.add(Monster1)
        for monster in Monsters:
            if pygame.sprite.collide_mask(tower, monster):
                monster.remove(Monsters)
                tower.health = tower.health - 50
            now = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if key[pygame.K_SPACE]:
                    if now - player.last_shot > player.cooldown:
                        monster.hp -= player.attack
                        monster.rect.x -= player.repulsion
                        monster.last_shot = now
            if monster.hp <= 0:
                monster.remove(Monsters)
        # updates
        screen.blit(background, [0, 0])
        player.draw(screen)
        tower.draw_tower(screen)
        player.update()
        Monsters.draw(screen)
        Monsters.update()
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
screen.fill((0, 0, 0))
pygame.display.update()
mainmenu()