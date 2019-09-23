# -*- coding: utf-8 -*-
import sys,pygame
from pygame.locals import *

class Arco (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("imagenes/Arco.png")
        self.rectangulo= self.imagen.get_rect()
        self.rectangulo.centerx=x
        self.rectangulo.centery=y
