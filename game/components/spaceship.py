
from pygame.sprite import Sprite
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_WIDTH

class Spaceship(Sprite):
    
    SHIP_WIDTH = 60
    SHIP_HEIGHT = 80
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 520
    SHIP_SPEED = 10
    LIMIT_UP = 0
    LIMIT_DOWN = 520
    LIMIT_LEFT = -30
    LIMIT_RIGHT = 1090
    
    def __init__(self):
        self.image  =  SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH,self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_x]:
            self.shoot(game.bullet_manager)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def move_left(self):
        if self.rect.x == self.LIMIT_LEFT:
            self.rect.x = 1090
        else:
            self.rect.x -= self.SHIP_SPEED
    
    def move_right(self):
        if self.rect.x == self.LIMIT_RIGHT:
            self.rect.x = -30
        else: 
            self.rect.x += self.SHIP_SPEED
    
    def move_up(self):
        if self.rect.y != self.LIMIT_UP:
            self.rect.y -= self.SHIP_SPEED
    
    def move_down(self):
        if self.rect.y != self.LIMIT_DOWN:
            self.rect.y += self.SHIP_SPEED
            
    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)