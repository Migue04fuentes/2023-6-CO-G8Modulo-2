import pygame
import os

pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUND_DIR = os.path.join(os.path.dirname(__file__),"..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_START = pygame.image.load(os.path.join(IMG_DIR, 'Other/background_start1.png'))
BG_END = pygame.image.load(os.path.join(IMG_DIR, 'Other/BG_END.webp'))

# HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship2.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship2_shield2.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

# Power UP
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
CLEAN = pygame.image.load(os.path.join(IMG_DIR, 'Other/clean.png'))
UP_BULLETS = pygame.image.load(os.path.join(IMG_DIR, 'Other/bullets.png'))

#Images of enemy ships
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, 'Enemy/enemy_3.png'))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, 'Enemy/enemy_4.png'))

#ICONS
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))
COINS = pygame.image.load(os.path.join(IMG_DIR, 'Other/coins.png'))
SCORE = pygame.image.load(os.path.join(IMG_DIR,('Other/ship_score.png')))
SCORE_DEATH = pygame.image.load(os.path.join(IMG_DIR,('Other/death_score_img.png')))
SCORE_TIME = pygame.image.load(os.path.join(IMG_DIR,('Other/time.png')))
RESET = pygame.image.load(os.path.join(IMG_DIR,('Other/reset1.png')))

#Game sound
# SOUND_PLAY = pygame.mixer.music.load(os.path.join(SOUND_DIR, "Sound/play.mp3"))
SOUND_PLAY = os.path.join(SOUND_DIR, 'Sound/play.mp3')
SOUND_TRANSPOSE =  pygame.mixer.Sound(os.path.join(SOUND_DIR, 'Sound/transpose.mp3'))
SHOT_SHIP = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'Sound/shot_ship.mp3'))
SOUND_COIN = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'Sound/coins.mp3'))
SOUND_GAME_OVER = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'Sound/game_over.mp3'))
SOUND_BANG= pygame.mixer.Sound(os.path.join(SOUND_DIR, 'Sound/bang.mp3'))
SOUND_POWER= pygame.mixer.Sound(os.path.join(SOUND_DIR, 'Sound/power_up.mp3'))


FONT_STYLE = 'freesansbold.ttf'
