'''
Created on 18/07/2015

@author: Mads
'''
import pygame

def initialize_screeen(size, caption):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    return screen

def draw_screen(screen, image):
    screen.blit(image , [0, 0])
