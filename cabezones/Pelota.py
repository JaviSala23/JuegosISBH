#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,pygame
from pygame.locals import *

class Pelota (pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("imagenes/PELOTA1.png")
        self.rectangulo= self.imagen.get_rect()
        self.rectangulo.centerx=x
        self.rectangulo.centery=y
        self.velocidad=velocidad
        self.izq=self.rectangulo.fit(0,40,40,40)

    def colision(self, objeto):
        return self.izq.colliderect(objeto)



