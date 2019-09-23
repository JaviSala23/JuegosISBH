# -*- coding: utf-8 -*-
#!/usr/bin/env python


# Módulos
import sys, pygame
from pygame.locals import *
pygame.init()

pop= pygame.mixer.Sound("sonido/pop.wav")


class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,ladrillo,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        la=["imagenes/ladriamarillo.png","imagenes/ladriapiel.png","imagenes/ladriazul.png","imagenes/ladrician.png","imagenes/ladrinara.png","imagenes/ladrirojo.png","imagenes/ladrirosa.png","imagenes/ladriverde.png"]
        self.image = pygame.image.load(la[ladrillo])
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
    def colision(self,bola,time):
        punto=0
        if pygame.sprite.collide_rect(self, bola):
            pygame.mixer.Sound.play(pop)
            self.rect.centerx=3000
            self.rect.centery=3000
            bola.speed[1] = -bola.speed[1]
            bola.rect.centery += bola.speed[1] * time
            punto=100
        return punto
