import Variables as variables
import pygame
import main 
from Character import Character
import Vector

class boss(Character):
	def __init__(self, image, colorKEY):
		super().__init__(image, colorKEY)
        self.x = 950
        self.y = 300
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 25

    def set_move(self, Target_x, Target_y):
        vec = Vector.vector([self.x,self.y],[Target_x, Target_y])
        x, y = vec.unit()
        self.change_x = x * self.speed 
        self.change_y = y * self.speed

def boos_fight(game_instance):

	return