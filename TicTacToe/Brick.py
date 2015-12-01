'''
Created on 18/07/2015

@author: Mads
'''
import pygame

class brick(pygame.sprite.Sprite):
    def __init__(self, image, colorKEY):
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = image
        self.image.set_colorkey(colorKEY)
    
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])