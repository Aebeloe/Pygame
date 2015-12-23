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
import Enemy
import redDot
import pygbutton
import Highscore

pygame.init()
HIGHSCORES = Highscore.Highscores()

class Game():
    def __init__(self):
        self.screen = initialize_screeen(variables.size, "Main Window")
        self.background_image = pygame.image.load(variables.BACKGROUND_IMAGE).convert()
        self.StartButton = pygbutton.PygButton((300, 500, 100, 40), 'Start Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("C:/Windows/Fonts/Gabriola.TTF",25)
        self.welcome_font = pygame.font.Font("C:/Windows/Fonts/Gabriola.TTF",50)
        self.score_font = pygame.font.Font("C:/Windows/Fonts/Gabriola.TTF", 30)
        self.Score = None

    def main(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if 'click' in self.StartButton.handleEvent(event):
                    Game = Instance(self.screen)
                    msg = Game.pregame()
                    if msg['text'] == 'quit':
                        done = True
                        continue
                    elif msg['text'] == 'back':
                        self.Score = msg['score']
                        HIGHSCORES.new_score(self.Score)
                        HIGHSCORES.scoreboard.sort(key=int, reverse=True)
                        continue
                    elif msg['text'] == 'dead':
                        self.Score = msg['score']
                        HIGHSCORES.new_score(self.Score)
                        HIGHSCORES.scoreboard.sort(key=int, reverse=True)
                        continue
                if event.type == pygame.QUIT:
                    done = True
            
            text = self.welcome_font.render('Velkommen til Princess Adventure', True, variables.BLUE)
            draw_screen(self.screen, self.background_image)
            self.screen.blit(text,[100, 400])
            if len(HIGHSCORES.scoreboard) > 0:
                highscore_text = self.score_font.render("Highscoren er: {}".format(HIGHSCORES.scoreboard[0]), True, variables.BLUE)
                self.screen.blit(highscore_text,[100, 350])
            if self.Score != None:
                score_text = self.score_font.render("Din Score var: {}".format(self.Score), True, variables.BLUE)
                self.screen.blit(score_text, [150, 450])

            self.StartButton.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(variables.fps)
        HIGHSCORES.save_score()

class Instance():
    def __init__(self, screen):
        self.screen = screen
        self.PRINCESS_FRONT_image = pygame.image.load("Sprites/princess_front.png").convert()
        self.PRINCESS_BACK_image = pygame.image.load("Sprites/princess_back.png").convert()
        self.PRINCESS_LEFT_image = pygame.image.load("Sprites/princess_left.png").convert()
        self.PRINCESS_RIGHT_image = pygame.image.load("Sprites/princess_right.png").convert()
        self.RED_DOT_image = pygame.image.load("Sprites/red_dot.png").convert()
        self.CANNON_image = pygame.image.load("Sprites/Cannon_ready.jpg").convert()
        self.CANNON_image.set_colorkey(variables.WHITE)
        self.CANNON_FIRE_image = pygame.image.load("Sprites/fire.jpg").convert()
        self.CANNON_FIRE_image.set_colorkey(variables.WHITE)

        self.FIREBALL_image = pygame.image.load("Sprites/red_dot.png").convert()

        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(variables.BACKGROUND_IMAGE).convert()
        self.back_button = pygbutton.PygButton((0, 0, 50, 40), 'Back')

        self.Princess = char.Character(self.PRINCESS_FRONT_image, variables.PRINCESS_BACKGROUND_FRONT)
        self.Princess.x = 500
        self.Princess.y = 400

        self.all_sprites_list = pygame.sprite.Group()

        self.all_health = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_red_dots = pygame.sprite.Group()
    
        self.all_sprites_list.add(self.Princess)
        self.font = pygame.font.Font("C:/Windows/Fonts/Gabriola.TTF",25)
        self.score = 0

        self.health_count = 0
        self.red_dot_time = 0

        self.all_arrows = pygame.sprite.Group()

        ANTAL_PILE = 10
        for i in range(ANTAL_PILE):
            a = Arrow.arrow()
            self.all_arrows.add(a)
            self.all_sprites_list.add(a)

        self.time_played = 0
    
        self.frames = 0
        self.draw_fire = 0

        

    def pregame(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return self.run()
                if event.type == pygame.QUIT:
                    return {'text': 'quit'}
            text = self.font.render("Tryk på en knap for at starte", True, variables.BLUE)
            draw_screen(self.screen, self.background_image)
            self.screen.blit(text,[500, 400])            
            pygame.display.flip()
            self.clock.tick(variables.fps)

    def run(self):
        done = False
        paused = False
        while not done:
            for event in pygame.event.get():
                if 'click' in self.back_button.handleEvent(event):
                    return {'text': 'back', 'score': score}
                if event.type == pygame.QUIT:
                    return {'text': 'quit'}
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.Princess.change_y = self.Princess.speed
                        self.Princess.change_direction(self.PRINCESS_FRONT_image, variables.PRINCESS_BACKGROUND_FRONT)
                    if event.key == pygame.K_LEFT:
                            self.Princess.change_x = -self.Princess.speed
                            self.Princess.change_direction(self.PRINCESS_RIGHT_image, variables.PRINCESS_BACKGROUND_BACK)
                    if event.key == pygame.K_RIGHT:
                        self.Princess.change_x = self.Princess.speed
                        self.Princess.change_direction(self.PRINCESS_LEFT_image, variables.PRINCESS_BACKGROUND_BACK)
                    if event.key == pygame.K_UP:
                        self.Princess.change_y = -self.Princess.speed 
                        self.Princess.change_direction(self.PRINCESS_BACK_image, variables.PRINCESS_BACKGROUND_BACK)
                    if event.key == pygame.K_SPACE:
                        paused = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.Princess.change_x = 0
                    if event.key == pygame.K_RIGHT:
                        self.Princess.change_x = 0
                    if event.key == pygame.K_UP:
                        self.Princess.change_y = 0
                    if event.key == pygame.K_DOWN:
                        self.Princess.change_y = 0
            if self.Princess.x < 10:
                if self.Princess.change_x < 0:
                    self.Princess.change_x = 0
            if self.Princess.x > 1014:
                if self.Princess.change_x > 0:
                    self.Princess.change_x = 0
            if self.Princess.y < 310:
                if self.Princess.change_y < 0:
                    self.Princess.change_y = 0
            if self.Princess.y > 670:
                if self.Princess.change_y > 0:     
                    self.Princess.change_y = 0

            if paused:
                while paused:
                    for event in pygame.event.get():
                        if 'click' in self.back_button.handleEvent(event):
                            return {'text': 'back', 'score': score}
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                paused = False
                                break
                        if event.type == pygame.QUIT:
                            return {'text': 'quit'}
            paused = False
            self.game_arrow_rain()

            pygame.display.flip()
            self.clock.tick(variables.fps)
    
    def fire_rain(self):


    def game_arrow_rain(self):    
        red_dot_interval = 500 #Hvor hurtigt kommer de røde bolde

        blocks_hit_list = pygame.sprite.spritecollide(self.Princess, self.all_arrows, True)
        health_hit_list = pygame.sprite.spritecollide(self.Princess, self.all_health,True)
        red_dot_hit_list = pygame.sprite.spritecollide(self.Princess, self.all_red_dots, False)
        enemy_hit_list = pygame.sprite.spritecollide(self.Princess, self.all_enemies, False)

        for hits in blocks_hit_list:
            self.Princess.hit()
            a = Arrow.arrow()
            self.all_arrows.add(a)
            self.all_sprites_list.add(a)
    
        for hits in health_hit_list:
            self.Princess.heal(hits.amount)

        for hits in red_dot_hit_list:
            self.Princess.heal(-100)
            self.all_red_dots.remove(hits)
            self.all_sprites_list.remove(hits)

        for hits in enemy_hit_list:
            #Hvad skal der ske når princessen rammer en sort prik
            continue

        if self.frames % variables.fps == 0:
            self.score = self.score + 1 
            
        text = self.font.render('HP: {}'.format(self.Princess.hp), True, variables.BLACK)
        score_text = self.font.render('Score: {}'.format(self.score), True, variables.RED)
        
        if self.health_count == 500:
            H_Box = Health.health()
            self.all_sprites_list.add(H_Box)
            self.all_health.add(H_Box)
            self.health_count = 0
    
        if self.red_dot_time == red_dot_interval:
            red_dot = redDot.reddot(self.RED_DOT_image, variables.WHITE)
            red_dot.set_move(float(self.Princess.x), float(self.Princess.y))
            self.all_sprites_list.add(red_dot)
            self.all_red_dots.add(red_dot)
            draw_fire = 100
            self.red_dot_time = 0
    
        else:
            self.red_dot_time += 1
        
        for health in self.all_health:
            health.counter += 1
            if health.counter == health.time:
                self.all_health.remove(health)
                self.all_sprites_list.remove(health)
        
        for enemy in self.all_enemies:
            enemy.move(self.Princess.x, self.Princess.y)
            
        self.health_count += 1
    
        for sprite in self.all_sprites_list:
            sprite.move()
        
        for arrow in self.all_arrows:
            if arrow.x < 0:
                arrow.x = random.randrange(1000, 1500)
                arrow.y = random.randrange(300,680)
    
        if self.Princess.hp <= 0:
            return {'text': 'dead', 'score': self.score}
        
        self.frames = self.frames + 1   
        if self.frames % 1800 == 0:
            NYE_PILE = 10
            for i in range(NYE_PILE):
                a = Arrow.arrow()
                self.all_arrows.add(a)
                self.all_sprites_list.add(a)
    
        draw_screen(self.screen, self.background_image)
        self.screen.blit(self.CANNON_image, [820, 20])
    
        if self.draw_fire > 0:
            self.screen.blit(self.CANNON_FIRE_image, [700, -25])
            self.draw_fire = self.draw_fire - 1
        self.screen.blit(text,[500, 0])
        self.screen.blit(score_text,[200, 0])			
        self.back_button.draw(self.screen)
    
        for sprite in self.all_sprites_list:
            sprite.draw(self.screen)
        
        return
    
if __name__ == "__main__":
    game = Game()
    game.main()