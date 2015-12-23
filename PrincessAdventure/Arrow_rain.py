import Arrow
import pygame
import Variables as variables
import Health

class Arrow_rain():
    def __init__(self, game_instance):
        self.all_arrows = pygame.sprite.Group()
        self.all_health = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_red_dots = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(game_instance.Princess)

        self.health_count = 0
        self.red_dot_time = 0

        ANTAL_PILE = 10
        for i in range(ANTAL_PILE):
            a = Arrow.arrow()
            self.all_arrows.add(a)
            self.all_sprites_list.add(a)

    def game_arrow_rain(self, game_instance):
        red_dot_interval = 500 #Hvor hurtigt kommer de røde bolde    
        blocks_hit_list = pygame.sprite.spritecollide(game_instance.Princess, self.all_arrows, True)
        health_hit_list = pygame.sprite.spritecollide(game_instance.Princess, self.all_health,True)
        red_dot_hit_list = pygame.sprite.spritecollide(game_instance.Princess, self.all_red_dots, False)
        enemy_hit_list = pygame.sprite.spritecollide(game_instance.Princess, self.all_enemies, False)        

        for hits in blocks_hit_list:
            game_instance.Princess.hit()
            a = Arrow.arrow()
            self.all_arrows.add(a)
            self.all_sprites_list.add(a)    

        for hits in health_hit_list:
            game_instance.Princess.heal(hits.amount)    
        
        for hits in red_dot_hit_list:
            game_instance.Princess.heal(-100)
            self.all_red_dots.remove(hits)
            self.all_sprites_list.remove(hits)    

        for hits in enemy_hit_list:
            #Hvad skal der ske når princessen rammer en sort prik
            continue    

        if game_instance.frames % variables.fps == 0:
            game_instance.score = self.score + 1 
            
        text = game_instance.font.render('HP: {}'.format(game_instance.Princess.hp), True, variables.BLACK)
        score_text = self.font.render('Score: {}'.format(game_instance.score), True, variables.RED)
        
        if game_instance.health_count == 500:
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


