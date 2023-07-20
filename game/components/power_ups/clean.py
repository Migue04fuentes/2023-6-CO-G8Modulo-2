
import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import CLEAN


class Clean(PowerUp):
    def __init__(self):
        self.image = CLEAN
        self.image = pygame.transform.scale(self.image,(35,35))
        super().__init__(self.image,'clean')