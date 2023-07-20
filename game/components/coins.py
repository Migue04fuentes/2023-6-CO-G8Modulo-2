import pygame
from game.utils.constants import COINS,FONT_STYLE

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
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.num_coins = 0
        
    def update(self,coin_speed):
        self.rect.y += coin_speed
    
    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 20)
        fontText = font.render('100',True,self.GRAY)
        fontRect = fontText.get_rect()
        fontRect.center = (53,55)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(fontText,(22,48))
        
