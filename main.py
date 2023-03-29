import pygame
from data import* 
from shooter_object import*

pygame.init()
window = pygame.display.set_mode((setting_win["WIDTH"],setting_win["HEIGHT"]))


def run():
    game = True
    hero = Hero(setting_win["WIDTH"]//2 -50,
                setting_win["HEIGHT"]-150,
                100,100,5,(255,0,0))


    while game:
        window.fill((0,0,0))
        pygame.draw.rect(window,hero.IMAGE,hero)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        pygame.display.flip()

run()