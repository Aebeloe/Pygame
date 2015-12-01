'''
Created on 17/07/2015

@author: Mads
'''
import Variables as variables
import pygame
from setup import initialize_screeen, draw_screen
import Character as char
import Arrow
import Health
import random

pygame.init()

def main():

    screen = initialize_screeen(variables.size, "Main Window")
    PRINCESS_FRONT_image = pygame.image.load("Sprites/princess_front.png").convert()
    PRINCESS_BACK_image = pygame.image.load("Sprites/princess_back.png").convert()
    PRINCESS_LEFT_image = pygame.image.load("Sprites/princess_left.png").convert()
    PRINCESS_RIGHT_image = pygame.image.load("Sprites/princess_right.png").convert()
    enemy_image = pygame.image.load("Sprites/enemy.png").convert()
    RED_DOT_image = pygame.image.load("Sprites/red_dot.png").convert()
    
    clock = pygame.time.Clock()
    done = False
    background_image = pygame.image.load(variables.BACKGROUND_IMAGE).convert()
    
    Princess = char.Character(PRINCESS_FRONT_image, variables.PRINCESS_BACKGROUND_FRONT)
    Enemy_1 = char.Character(enemy_image, variables.WHITE)
    Enemy_2 = char.Character(enemy_image, variables.WHITE)
    
    Enemy_1.x = 600
    Enemy_1.y = 236
    Enemy_2.x = 342
    Enemy_2.y = 534
    
    all_sprites_list = pygame.sprite.Group()
    all_arrows = pygame.sprite.Group()
    all_health = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    #move_ables= pygame.sprite.Group() en god ide hvis man har ting der aldrig skal beveage sig ellers skal alle sprites have move()
    
    all_sprites_list.add(Princess)
    all_sprites_list.add(Enemy_1)
    all_sprites_list.add(Enemy_2)
    all_enemies.add(Enemy_1)
    all_enemies.add(Enemy_2)
    font = pygame.font.Font("C:/Windows/Fonts/Gabriola.TTF",25)
    
    ANTAL_PILE = 100
    for i in range(ANTAL_PILE ):
        a = Arrow.arrow()

        
        all_arrows.add(a)
        all_sprites_list.add(a)
        
    health_count = 0    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Princess.change_y = Princess.speed
                    Princess.change_direction(PRINCESS_FRONT_image, variables.PRINCESS_BACKGROUND_FRONT)
                if event.key == pygame.K_LEFT:
                    Princess.change_x = -Princess.speed
                    Princess.change_direction(PRINCESS_RIGHT_image, variables.PRINCESS_BACKGROUND_BACK)
                if event.key == pygame.K_RIGHT:
                    Princess.change_x = Princess.speed
                    Princess.change_direction(PRINCESS_LEFT_image, variables.PRINCESS_BACKGROUND_BACK)
                if event.key == pygame.K_UP:
                    Princess.change_y = -Princess.speed 
                    Princess.change_direction(PRINCESS_BACK_image, variables.PRINCESS_BACKGROUND_BACK)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Princess.change_x = 0
                if event.key == pygame.K_RIGHT:
                    Princess.change_x = 0
                if event.key == pygame.K_UP:
                    Princess.change_y = 0
                if event.key == pygame.K_DOWN:
                    Princess.change_y = 0    
        
        blocks_hit_list = pygame.sprite.spritecollide(Princess, all_arrows, True)
        healt_hit_list = pygame.sprite.spritecollide(Princess,all_health,True)
        
        for hits in blocks_hit_list:
            Princess.hit()
            a = Arrow.arrow()
            all_arrows.add(a)
            all_sprites_list.add(a)
        
        for hits in healt_hit_list:
            Princess.heal(hits.amount)
            
        text = font.render('HP: {}'.format(Princess.hp), True, variables.BLACK)
        
        if health_count == 500:
            H_Box = Health.health()
            all_sprites_list.add(H_Box)
            all_health.add(H_Box)
            health_count = 0
        
        if health_count % 100 == 0:
            red_dot = char.Character(RED_DOT_image, variables.WHITE)
            red_dot.red_Dot_Move(float(Princess.x), float(Princess.y))
            all_sprites_list.add(red_dot)

            
        for health in all_health:
            health.counter += 1
            if health.counter == health.time:
                all_health.remove(health)
                all_sprites_list.remove(health)
            
        Enemy_1.enemy_move(Princess.x, Princess.y)
        Enemy_2.enemy_move(Princess.x, Princess.y)
        
        
        health_count += 1
        for sprite in all_sprites_list:
            sprite.move()
        
        for arrow in all_arrows:
            arrow.move()    
            if arrow.x < 0:
                arrow.x = random.randrange(1000,1500)
                arrow.y = random.randrange(700)
        
        draw_screen(screen, background_image)
        screen.blit(text,[500,0])
        for sprite in all_sprites_list:
            sprite.draw(screen)
            
        pygame.display.flip()
        clock.tick(variables.fps)

    return

if __name__ == "__main__":
    main()