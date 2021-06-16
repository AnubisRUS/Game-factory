import pygame
from settings import *
import pygame, sys, time

#import sprites
from sprites.buttons import *

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

    #sprites
    test_text = arial.render("GameFactory", True, (255, 255, 255))

    running = True
    screen.fill((0, 0, 0))
    screen.blit(test_text, (410, 300))
    pygame.display.update()
    time.sleep(5)
    while running:
        clock.tick(FPS)
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # rendering
        screen.fill((0, 0, 0))

        # updates
        pygame.display.update()

def tutorial():
    # fonts
    arial = pygame.font.SysFont("Arial", 72)

    #sprites
    test_text = arial.render("Tutorial", True, (255, 255, 255))

    running = True
    while running:

        clock.tick(FPS)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # rendering
        screen.fill((0, 0, 0))
        screen.blit(test_text, (410, 300))

        # update
        pygame.display.update()



#showing menu
mainmenu()