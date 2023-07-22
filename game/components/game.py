import pygame
from game.components.bullets.bullet_manager import bulletManager
from game.components.Coins.coin_manager import CoinManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

from game.utils.constants import BG, BG_END, BUY, COINS, FONT_STYLE, HEART, ICON, ICON_EXIT, ICON_MUSIC, ICON_MUSIC_MUTE, ICON_PAUSE, ICON_PLAY, ICON_RESET, IMG_PAUSE, RESET, SCORE, SCORE_DEATH, SCORE_TIME, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SOUND_PLAY
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.heart import Heart

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
        self.coin_manager = CoinManager()
        self.heart = Heart()
        self.death_score = 0
        self.score = 0
        self.time = 0
        self.num_heart = 3
        self.coins = 5
        self.pause = False
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
        pygame.mixer.music.set_volume(0.1)
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
        self.player.update(user_input,self,self.screen)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.coin_manager.update(self)
        self.power_up_manager.update(self)
        
        

    def draw(self,game):
        self.clock.tick(FPS)
        # self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.coin_manager.draw(self.screen)
        self.draw_power_up_time()
        self.heart.draw(self.screen,game)

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
        
        icon_coin = pygame.transform.scale(COINS, (20,25))
        self.screen.blit(icon_coin,(2,45))
        
        # VALUES OF SCORE
        self.menu.message_menu(self.screen,self.time,1020,20,20,'White')
        self.menu.message_menu(self.screen,self.score,28,77,20,'Blue')
        self.menu.message_menu(self.screen,self.coins,25,50,20,'White')
        
        # ICON OF MENÚ PLAYING
        self.menu.icons_menu(self.screen,ICON_PAUSE,1045,90,35,35)
        self.menu.icons_menu(self.screen,ICON_MUSIC,1045,130,35,35)
        self.menu.icons_menu(self.screen,ICON_RESET,1045,170,35,35)
        self.menu.icons_menu(self.screen,ICON_EXIT,1045,210,35,35)
        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_scree_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.num_heart == 0:
            image = pygame.transform.scale(BG_END, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(image,(0,0))
            self.menu.update_message("Statistics:")
            self.menu.message_menu(self.screen,"Game Over",420,100,50,'Blue')
            self.draw_score(self.screen)
            # Btn reset
            resets = self.menu.icons_menu(self.screen,RESET,480,500,150,40)
            self.click_reset(resets)
            #Btn Buy
            click_buy = self.coins_buy(self.screen)
            self.click_buy(click_buy)
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
        self.menu.icons_menu(screen,COINS,700,270,40,40)
        self.menu.message_menu(screen,self.coins,760,275,30,'Black')
        
    def coins_buy(self,screen):
        if self.coins >= 5:
            num_heart = self.coins//5
            self.menu.message_menu(screen,f'Buy a heart for 5 coins',390,355,32,'Black')
            self.menu.icons_menu(screen,HEART,480,400,35,35)
            self.menu.message_menu(screen,num_heart,525,403,32,'Black')
            click_buy = self.menu.icons_menu(screen,BUY,550,400,80,40)
            return [click_buy,num_heart]
    
        
    # Mute and Sound
    def mute_music(self):
        if pygame.mixer.music.get_volume() ==0.0:
            pygame.mixer.music.set_volume(0.1)
            self.menu.icons_menu(self.screen,ICON_MUSIC,1045,130,35,35)
        else:
            pygame.mixer.music.set_volume(0.0)
            self.menu.icons_menu(self.screen,ICON_MUSIC_MUTE,1045,130,35,35)
    
    def click_reset(self,img_reset):
        mouse = pygame.mouse.get_pos()
        if img_reset.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
                self.reset_game()
                self.run()
                
    def click_buy(self,img_buy):
        if self.coins >= 5:
            mouse = pygame.mouse.get_pos()
            if img_buy[0].collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
                    self.num_heart = img_buy[1]
                    self.coins -= (img_buy[1]*5)
                    self.run()
        
    def reset_game(self):
            self.enemy_manager.enemies = []
            self.death_score = 0
            self.score = 0
            self.coins = 0
            self.num_heart = 3
    
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