import pygame
from game.utils.constants import BG_START, FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu():
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT//2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH//2
    pos_x = SCREEN_HEIGHT - 100
    def __init__(self,message,screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE,25)
        self.text = self.font.render(message,True,(255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH,self.pos_x)
        self.color ={
            "White":(255,255,255),
            "Black":(0,0,0),
            "Blue":(100,166,255),
            "Red":(255,0,0)
        }
        

    def update(self,game):
        pygame.display.update()
        self.handle_events_on_menu(game)
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
    
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN and game.score==0 and game.death_score == 0:
                game.run()
    
    def reset_screen_color(self,screen):
        # screen.fill((255,255,255))
        image = pygame.transform.scale(BG_START, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image,(0,0))
    
    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (550,230)

    def message_menu(self,screen,message,pos_x,pos_y,font_size,color):
        color_text = self.color.get(color)
        font_message = pygame.font.Font(FONT_STYLE,font_size)
        text_message  = font_message.render(message, True, color_text)
        screen.blit(text_message,(pos_x,pos_y))
        
    def icons_menu(self,screen,images,pos_x,pos_y,width,height):
        # icon score menu
        images = pygame.transform.scale(images, (width,height))
        image_rect = images.get_rect()
        image_rect.x = pos_x
        image_rect.y = pos_y
        screen.blit(images,(pos_x,pos_y))
        return image_rect