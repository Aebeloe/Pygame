'''
Created on 17/07/2015

@author: Mads
'''
# tobiasj1991@gmail.com
# m.aebeloe@gmail.com

import pygame 
import Variables as variables

class Character(pygame.sprite.Sprite):
    def __init__(self, image, colorKEY):
        super().__init__()
        self.image = image
        self.image.set_colorkey(colorKEY)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.x = 0
        self.y = 0
        self.hp = 10
        self.rect.x = self.x
        self.rect.y = self.y 
        self.speed = 10
        
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        self.rect.x = self.x
        self.rect.y = self.y 
        
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])
    
    def hit(self):
        self.hp -= 1
    
    def heal(self, amount):
        self.hp += amount
        
    def change_direction(self, image, colorKEY):
        self.image = image
        self.image.set_colorkey(colorKEY)

    def sword_swing(self, direction, screen):
        return
