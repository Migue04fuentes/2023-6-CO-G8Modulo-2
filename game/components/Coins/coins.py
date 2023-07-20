import random
import pygame
from game.utils.constants import COINS,FONT_STYLE, SCREEN_HEIGHT

class Coins():
    pygame.init()
    GRAY = (210,210,210)
    BLUE = (0,0,0,0.9)
    C_WIDTH = 20
    C_HEIGHT = 25
    Y_POS = 45
    X_POS = 2
    
    
    def __init__(self):
        self.image = COINS
        self. image = pygame.transform.scale(self.image,(self.C_WIDTH,self.C_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10,1000)
        self.rect.y = self.Y_POS
        self.num_coins = 0
        self.start_time = 0
        self.power_time_up = 0
        
    def update(self,coin_speed, list_coins):
        self.rect.y += coin_speed
        if self.rect.y > SCREEN_HEIGHT:
            list_coins.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x  , self.rect.y))
        
    
        
