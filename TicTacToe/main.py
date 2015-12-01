'''
Created on 18/07/2015

@author: Mads
'''
import pygame
import Variables as variables
from setup import initialize_screeen, draw_screen
import Brick

def main():
    screen = initialize_screeen(variables.size, "Tic Tac Toe")
    clock = pygame.time.Clock()
    done = False
    background_image = pygame.image.load(variables.back_ground_img).convert()
    kryds_image = pygame.image.load(variables.kryds_img).convert()
    bolle_image = pygame.image.load(variables.bolle_img).convert()
    
    all_bricks = pygame.sprite.Group()
    
    turn = 'player1'
    pos1 = 0
    pos2 = 0
    pos3 = 0
    pos4 = 0 
    pos5 = 0
    pos6 = 0
    pos7 = 0
    pos8 = 0
    pos9 = 0
    placed = False
    
    b = Brick.brick(kryds_image, variables.WHITE)
    all_bricks.add(b)
    
    turn_count = 1
    while not done:
        posX, posY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if posX < 60:
                    if posY < 63:
                        if turn == 'player1':
                            pos1 = 1
                        else:
                            pos1 = 2    
                    elif posY > 137:
                        if turn == 'player1':
                            pos7 = 1
                        else:
                            pos7 = 2 
                    else:
                        if turn == 'player1':
                            pos4 = 1
                        else:
                            pos4 = 2
                elif posX > 135:
                    if posY < 63:
                        if turn == 'player1':
                            pos3 = 1
                        else:
                            pos3 = 2
                    elif posY > 137:
                        if turn == 'player1':
                            pos9 = 1
                        else:
                            pos9 = 2
                    else:
                        if turn == 'player1':
                            pos6 = 1
                        else:
                            pos6 = 2
                else:
                    if posY < 63:
                        if turn == 'player1':
                            pos2 = 1
                        else: 
                            pos2 = 2
                    elif posY > 137:
                        if turn == 'player1':
                            pos8 = 1
                        else:
                            pos8 = 2
                    else:
                        if turn == 'player1':
                            pos5 = 1
                        else:
                            pos5 = 2
                
                placed = True
                if turn == 'player1':
                    turn = 'player2'
                else:
                    turn = 'player1'
                
                turn_count += 1 
                
        if turn == 'player1' and placed:
            b = Brick.brick(kryds_image, variables.WHITE)
            all_bricks.add(b)
            placed = False
        
        if turn == 'player2' and placed:
            b = Brick.brick(bolle_image, variables.WHITE)
            all_bricks.add(b)
            placed = False
        
        win = check_for_Win(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
        if win == 'player1':
            print ('Kryds Vandt')
        elif win == 'player2':
            print ('Bolle Vandt')
        elif turn_count == 9:
            print ('Draw')
        
        b.x = posX - 28
        b.y = posY - 28
        
        draw_screen(screen, background_image)
        for brick in all_bricks:
            brick.draw(screen)
        
        pygame.display.flip()

def check_for_Win(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):
    if pos1 == pos2 == pos3:
        if pos1 == 1:
            return 'player1'
        elif pos1 == 2: 
            return 'player2'
    elif pos4 == pos5 == pos6:
        if pos4 == 1:
            return 'player1'
        elif pos4 == 2: 
            return 'player2'
    elif pos7 == pos8 == pos9:
        if pos7 == 1:
            return 'player1'
        elif pos7 == 2: 
            return 'player2'
    elif pos1 == pos4 == pos7:
        if pos1 == 1:
            return 'player1'
        elif pos1 == 2: 
            return 'player2'
    elif pos2 == pos5 == pos8:
        if pos2 == 1:
            return 'player1'
        elif pos2 == 2: 
            return 'player2'
    elif pos3 == pos6 == pos9:
        if pos3 == 1:
            return 'player1'
        elif pos3 == 2: 
            return 'player2'
    elif pos1 == pos5 == pos9:
        if pos1 == 1:
            return 'player1'
        elif pos1 == 2: 
            return 'player2'
    elif pos3 == pos5 == pos7:
        if pos3 == 1:
            return 'player1'
        elif pos3 == 2: 
            return 'player2'
    else:
        return ''


if __name__ == "__main__":
    main()