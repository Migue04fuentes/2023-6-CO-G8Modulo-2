
from pygame.sprite import Sprite
import pygame
from game.components.bullets.bullet import Bullet

from game.utils.constants import DEFAULT_TYPE, ICON_MUSIC, ICON_MUSIC_MUTE, ICON_PLAY, IMG_PAUSE, SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH, SOUND_TRANSPOSE, SOUND_PLAY

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
        # pygame.init()
        self.image  =  SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH,self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = ''
        self.power_up_type = DEFAULT_TYPE
        self.power_time_up = 0

    def update(self, user_input,game,screen):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        
        # Volume music background
        if user_input[pygame.K_m]:
            self.mute_music(game,screen)
            # if pygame.mixer.music.get_volume() ==0.0:
            #     pygame.mixer.music.set_volume(0.5)
            # else:
            #     pygame.mixer.music.set_volume(0.0)
        
        if user_input[pygame.K_x]:
            self.shoot(game)
            
        if user_input[pygame.K_p]:
            self.paused(game,screen)
            
        if user_input[pygame.K_r]:
            game.playing = False
            pygame.mixer.music.stop()
            game.reset_game()
            game.run
            
        if user_input[pygame.K_BACKSPACE] or user_input[pygame.K_ESCAPE]:
            game.running = False
            game.playing = False
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def move_left(self):
        if self.rect.x == self.LIMIT_LEFT:
            self.rect.x = 1090
            SOUND_TRANSPOSE.play()
        else:
            self.rect.x -= self.SHIP_SPEED
    
    def move_right(self):
        if self.rect.x == self.LIMIT_RIGHT:
            self.rect.x = -30
            SOUND_TRANSPOSE.play()
        else: 
            self.rect.x += self.SHIP_SPEED
    
    def move_up(self):
        if self.rect.y != self.LIMIT_UP:
            self.rect.y -= self.SHIP_SPEED
    
    def move_down(self):
        if self.rect.y != self.LIMIT_DOWN:
            self.rect.y += self.SHIP_SPEED
            
    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet,self,game)
        
    def set_image(self,size = (SHIP_WIDTH,SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        
    def paused(self,game,screen):
        if game.pause:
            game.pause = False
            # game.playing = True
        else: 
            game.pause = True
            # game.playing = False
            image = pygame.transform.scale(IMG_PAUSE, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(image,(0,0))
        
    # Mute and Sound
    def mute_music(self,game,screen):
        if pygame.mixer.music.get_volume() == 0.0:
            pygame.mixer.music.set_volume(0.1)
            game.menu.icons_menu(screen,ICON_MUSIC,900,130,35,35)
            print('No Mute')
        else:
            pygame.mixer.music.set_volume(0.0)
            game.menu.icons_menu(screen,ICON_MUSIC_MUTE,1045,130,35,35)
            print('Mute')