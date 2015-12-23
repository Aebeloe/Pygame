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
import Arrow_rain

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
        self.FIREBALL_image = pygame.image.load("Sprites/red_dot.png").convert()

        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(variables.BACKGROUND_IMAGE).convert()
        self.back_button = pygbutton.PygButton((0, 0, 50, 40), 'Back')

        self.Princess = char.Character(variables.PRINCESS_FRONT_image, variables.PRINCESS_BACKGROUND_FRONT)
        self.Princess.x = 500
        self.Princess.y = 400

        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.Princess)
        self.font = pygame.font.Font("C:/Windows/Fonts/Gabriola.TTF",25)
        self.score = 0

        self.health_count = 0
        self.red_dot_time = 0


        self.time_played = 0
    
        self.frames = 0
        self.draw_fire = 0
        self.arrow_rain_instance = Arrow_rain.Arrow_rain()



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
                        self.Princess.change_direction(variables.PRINCESS_FRONT_image, variables.PRINCESS_BACKGROUND_FRONT)
                    if event.key == pygame.K_LEFT:
                            self.Princess.change_x = -self.Princess.speed
                            self.Princess.change_direction(variables.PRINCESS_RIGHT_image, variables.PRINCESS_BACKGROUND_BACK)
                    if event.key == pygame.K_RIGHT:
                        self.Princess.change_x = self.Princess.speed
                        self.Princess.change_direction(variables.PRINCESS_LEFT_image, variables.PRINCESS_BACKGROUND_BACK)
                    if event.key == pygame.K_UP:
                        self.Princess.change_y = -self.Princess.speed 
                        self.Princess.change_direction(variables.PRINCESS_BACK_image, variables.PRINCESS_BACKGROUND_BACK)
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
                            return {'text': 'back', 'score': self.score}
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
    
if __name__ == "__main__":
    game = Game()
    game.main()