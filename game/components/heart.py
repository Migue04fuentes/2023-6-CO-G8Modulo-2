import pygame
from game.utils.constants import HEART

class Heart():
    
    HEART_WIDTH= 80
    HEART_HEIGHT=40
    X_POS = -5
    Y_POS = 5
    
    def __init__(self):
        self.image = HEART
        self.image = pygame.transform.scale(self.image,(self.HEART_WIDTH,self.HEART_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
        