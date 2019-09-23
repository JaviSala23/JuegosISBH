#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
pygame.init()
metal= pygame.mixer.Sound("sonido/metal.wav")
# Constantes

class Bola(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/pelotaroja.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.30, -0.30]


    def actualizar(self, time,WIDTH,HEIGHT,pala):
        a=0

        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time


        if self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <=0:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
        if self.rect.top>=HEIGHT:
            a=1
            self.rect.centerx=WIDTH/2
            self.rect.centery=HEIGHT-100
        if pygame.sprite.collide_rect(self, pala):
            pygame.mixer.Sound.play(metal)
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time


        return a