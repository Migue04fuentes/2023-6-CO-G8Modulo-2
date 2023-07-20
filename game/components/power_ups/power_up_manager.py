import random

import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.power_ups.bullets_up import BulletUp
from game.components.power_ups.clean import Clean
from game.components.power_ups.shield import Shield

from game.utils.constants import SOUND_POWER, SPACESHIP_SHIELD


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3,5)
        self.when_appears = random.randint(1000,10000)
        self.enemy = EnemyManager()
        
    def update(self,game):
        current_time = pygame.time.get_ticks()
     
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
           self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                if power_up.type == 'shield':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = 'shield'
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.set_image((65,75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
                if power_up.type == 'bullets':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = 'bullets'
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)
                if power_up.type == 'clean':
                    for enemy in game.enemy_manager.enemies:
                        game.enemy_manager.enemies.remove(enemy)
                        game.score +=1
                    self.power_ups.remove(power_up)
                SOUND_POWER.play()
     
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up = [Shield(), BulletUp(),Clean()]
        self.when_appears += random.randint(5000,10000)
        self.power_ups.append(power_up[random.randint(0,2)])
