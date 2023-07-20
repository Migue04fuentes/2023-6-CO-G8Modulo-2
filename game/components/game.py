import pygame
from game.components.bullets.bullet_manager import bulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

from game.utils.constants import BG, BG_END, COINS, FONT_STYLE, ICON, RESET, SCORE, SCORE_DEATH, SCORE_TIME, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SOUND_PLAY
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.heart import Heart
from game.components.coins import Coins

class Game():
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = bulletManager()
        self.power_up_manager = PowerUpManager()
        self.heart = Heart()
        self.coins = Coins()
        self.death_score = 0
        self.score = 0
        self.time = 0
        self.num_heart = 3
        self.menu = Menu('Press Any Key To Start...', self.screen)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        pygame.mixer.music.load(SOUND_PLAY)
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.5)
        while self.playing:
            self.events()
            self.update()
            self.draw(self)
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.time = pygame.time.get_ticks()//1000
        self.power_up_manager.update(self)

    def draw(self,game):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.heart.draw(self.screen,game)
        self.coins.draw(self.screen)
        self.menu.message_menu(self.screen,self.time,1020,20,20,'White')
        self.menu.message_menu(self.screen,self.score,28,77,20,'Blue')
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
        
        # icon score play
        icon_score = pygame.transform.scale(SCORE, (20,25))
        self.screen.blit(icon_score,(3,73))
        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_scree_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_score > 0:
            image = pygame.transform.scale(BG_END, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(image,(0,0))
            self.menu.update_message("Statistics:")
            self.menu.message_menu(self.screen,"Game Over",420,100,50,'Blue')
            self.draw_score(self.screen)
            # Btn reset
            resets = self.menu.icons_menu(self.screen,RESET,480,500,150,40)
            self.click_reset(resets)
            self.playing = False
            pygame.mixer.music.stop()
        self.menu.draw(self.screen)
        self.menu.update(self)
        

    def update_score(self):
        self.score += 1
        
    def draw_score(self,screen):
        # Score
        self.menu.message_menu(screen,self.score,420,276,30,'Black')
        self.menu.icons_menu(screen,SCORE,360,265,50,50)
        
        # Death_Score
        self.menu.message_menu(screen,self.death_score,530,276,30,'Black')
        self.menu.icons_menu(screen,SCORE_DEATH,480,275,40,35)
        
        # Time_Score
        self.menu.message_menu(screen,self.time,634,277,30,'Black')
        self.menu.icons_menu(screen,SCORE_TIME,580,265,50,50)
        
        # Coins
        self.menu.icons_menu(screen,COINS,680,270,40,40)
        
        
    def click_reset(self,img_reset):
        mouse = pygame.mouse.get_pos()
        if img_reset.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
                self.reset_game()
                self.run()
        
    def reset_game(self):
        self.enemy_manager.enemies.pop()
        self.death_score = 0
        self.score = 0
        self.num_heart = 3
        self.time -=(pygame.time.get_ticks()//1000)
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()),2)
            
            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 20)
                text = font.render(f'Time {self.player.power_up_type.capitalize()} {time_to_show}',True,(255,255,255))
                text_rect = text.get_rect()                
                self.screen.blit(text,(900,60))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()