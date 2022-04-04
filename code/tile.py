import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        #Needed for every  kind of sprite
        self.image = pygame.image.load('C:\\Users\\marcd\\source\\repos\\PYRPG\\graphics\\test\\rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
