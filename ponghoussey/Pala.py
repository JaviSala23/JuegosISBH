#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
pygame.init()

# Constantes


class Pala(pygame.sprite.Sprite):
    def __init__(self, x,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5

    def mover(self, time, keys,HEIGHT):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
        if keys[K_ESCAPE]:
                        pygame.quit()
                        sys.exit()

    def ia(self, time, ball,WIDTH,HEIGHT):
        if ball.speed[0] >= 0 and ball.rect.centerx >= (WIDTH/2)+250:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time