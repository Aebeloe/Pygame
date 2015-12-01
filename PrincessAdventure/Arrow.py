'''
Created on 17/07/2015

@author: Mads
'''
import Variables as variables
import pygame
import random

class arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprites/arrow.png").convert()
        self.image.set_colorkey(variables.WHITE)
        self.rect = self.image.get_rect()
        self.change_x = -5
        self.change_y = 0
        self.x = random.randrange(1000,1500)
        self.y = random.randrange(700)
        self.rect.x = self.x
        self.rect.y = self.y
        
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])