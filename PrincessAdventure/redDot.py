'''
Created on 18/07/2015

@author: Mads
'''
import Character
import Vector

class reddot(Character.Character):
    def __init__(self, image, colorKEY):
        super().__init__(image, colorKEY)
        self.x = 860
        self.y = 85
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 20

    def set_move(self, Target_x, Target_y):
        vec = Vector.vector([self.x,self.y],[Target_x, Target_y])
        x, y = vec.unit()
        self.change_x = x * self.speed 
        self.change_y = y * self.speed