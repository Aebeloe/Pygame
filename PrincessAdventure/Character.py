'''
Created on 17/07/2015

@author: Mads
'''
import pygame 
import Variables as variables
import Vector

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
    
    def enemy_move(self, Target_x, Target_y):
        if Target_x < self.x:
            self.change_x = -7
        elif Target_x > self.x:
            self.change_x = 7
        else:
            self.change_x = 0
            
        if Target_y < self.y:
            self.change_y = -7
        elif Target_y > self.y:
            self.change_y = 7
        else:
            self.change_y = 0
            
    def red_Dot_Move(self, Target_x, Target_y):
        vec = Vector.vector([self.x,self.y],[Target_x, Target_y])
        x, y = vec.unit()
        self.change_x = x * 3 
        self.change_y = y * 3
        
        
        
        
        
        