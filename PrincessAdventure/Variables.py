'''
Created on 17/07/2015

@author: Mads
'''
import pygame 

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED  = (255,0,0)
BLUE = (0,0,225)
PRINCESS_BACKGROUND_FRONT = (82,170,49)
PRINCESS_BACKGROUND_BACK = (34,177,76)
fps = 50
size = [1024 ,700]
BACKGROUND_IMAGE = "Sprites/Castle.jpg"


PRINCESS_FRONT_image = pygame.image.load("Sprites/princess_front.png").convert()
PRINCESS_BACK_image = pygame.image.load("Sprites/princess_back.png").convert()
PRINCESS_LEFT_image = pygame.image.load("Sprites/princess_left.png").convert()
PRINCESS_RIGHT_image = pygame.image.load("Sprites/princess_right.png").convert()
RED_DOT_image = pygame.image.load("Sprites/red_dot.png").convert()
CANNON_image = pygame.image.load("Sprites/Cannon_ready.jpg").convert()
CANNON_image.set_colorkey(WHITE)
CANNON_FIRE_image = pygame.image.load("Sprites/fire.jpg").convert()
CANNON_FIRE_image.set_colorkey(WHITE)