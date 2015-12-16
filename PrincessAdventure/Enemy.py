'''
Created on 17/07/2015

@author: Mads
'''
import Character

class enemy(Character.Character):
    def __init__(self, image, colorKEY):
        super().__init__(image, colorKEY)

    def move(self, Target_x, Target_y):
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