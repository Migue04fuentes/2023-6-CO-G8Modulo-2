import pygame
from game.utils.constants import HEART

class Heart():
    
    HEART_WIDTH= 20
    HEART_HEIGHT=20
    X_POS = 3
    Y_POS = 15
    
    def __init__(self):
        self.image = HEART
        self.image = pygame.transform.scale(self.image,(self.HEART_WIDTH,self.HEART_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.num_heart = 3
        
    def update(self):
        pass
    
    def draw(self, screen,life):
        self.rect.x = self.X_POS
        for ejecucion in range(life.num_heart):
            screen.blit(self.image, (self.rect.x,self.rect.y))
            self.rect.x +=25
       
        