
import random

import pygame

from game.components.Coins.coins import Coins
from game.utils.constants import SOUND_COIN


class CoinManager:
    def __init__(self):
        self.list_coins = []
        self.duration = random.randint(5,10)
        self.when_appears = random.randint(10000,20000)
        
    def update(self,game):
        current_time = pygame.time.get_ticks()
            
        if len(self.list_coins) == 0 and  current_time>=self.when_appears:
            self.add_coin()
        
        for coin in self.list_coins:
            coin.update(game.game_speed,self.list_coins)
                
            if game.player.rect.colliderect(coin):
                coin.start_time = pygame.time.get_ticks()
                coin.power_time_up = coin.start_time + (self.duration * 1000)
                self.list_coins.remove(coin)
                game.coins += 1
                SOUND_COIN.play()
            break
            
    def draw(self,screen):
        for coin in self.list_coins:
            coin.draw(screen)
            
    def add_coin(self):
        coin = Coins()
        if len(self.list_coins)<1:
            self.list_coins.append(coin)
        self.when_appears += random.randint(5000,10000)