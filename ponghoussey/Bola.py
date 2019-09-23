#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
pygame.init()


# Constantes

class Bola(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/ball.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.10, -0.10]


    def actualizar(self, time, pala_jug, pala_cpu, puntos,WIDTH,HEIGHT):
        pygame.mixer.init()
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        if self.rect.left <= 0:
            puntos[1] += 1
        if self.rect.right >= WIDTH:
            puntos[0] += 1

        sonido=pygame.mixer.Sound('sonido/laser.ogg')

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time


        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            sonido.play()

        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            sonido.play()


        return puntos