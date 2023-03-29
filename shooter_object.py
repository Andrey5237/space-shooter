import pygame


class Hero(pygame.Rect):
    def __init__(self, x, y, width, height,speed,image):
        super().__init__(x, y, width, height)
        self.SPEED=speed
        self.IMAGE=image