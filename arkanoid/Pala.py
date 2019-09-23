#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
pygame.init()

# Constantes


class Pala(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/palan.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT - 30
        self.speed = 0.5

    def mover(self, time, keys,WIDTH):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
        if keys[K_ESCAPE]:
                        pygame.quit()
                        sys.exit()

    def ia(self, time, ball,WIDTH,HEIGHT):
        if ball.speed[0] >= 0 and ball.rect.centerx >= (WIDTH/2)+250:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time