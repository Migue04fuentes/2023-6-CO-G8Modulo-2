import pygame

from game.utils.constants import SHIELD_TYPE, SHOT_SHIP, SOUND_BANG, SOUND_GAME_OVER


class bulletManager():
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
    def update(self,game):
        
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != 'shield':
                    game.num_heart -=1
                    if game.num_heart == 0:
                        game.playing = False
                        pygame.time.delay(1000) 
                        SOUND_GAME_OVER.play()
                    SOUND_BANG.play()
                    game.death_score += 1
                break
        
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score +=1
                    
                     
    
    def draw(self,screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def add_bullet(self,bullet,game,enemies):
        num_enemies = len(enemies.enemy_manager.enemies)
        
        if bullet.owner == 'enemy' and len(self.enemy_bullets)<num_enemies:
            self.enemy_bullets.append(bullet)
           
        if bullet.owner == 'player' and game.power_up_type == 'bullets':
            self.bullets.append(bullet)
            SHOT_SHIP.set_volume(0.5)
            SHOT_SHIP.play() 
        elif bullet.owner == 'player' and len(self.bullets)<3:
            self.bullets.append(bullet)
            SHOT_SHIP.set_volume(0.5)
            SHOT_SHIP.play()
            
        