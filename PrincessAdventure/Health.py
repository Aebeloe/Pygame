'''
Created on 17/07/2015

@author: Mads
'''
import pygame
import Variables as variables
import random

class health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.amount = 5
        self.image = pygame.image.load("Sprites/health_box.png").convert()
        self.image.set_colorkey(variables.WHITE)
        self.rect = self.image.get_rect()
        self.x = random.randrange(1024)
        self.y = random.randrange(700)
        self.rect.x = self.x
        self.rect.y = self.y
        self.time = 500
        self.counter = 0
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def move(self):
        return