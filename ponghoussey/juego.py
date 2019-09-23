#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
import random
import Bola
import Pala
from pygame.locals import *
pygame.init()

# Constantes
WIDTH = 640
HEIGHT = 480


# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------
pygame.mixer.init()


def texto(texto, posx, posy, color=(0, 0, 0)):
    fuente = pygame.font.Font('imagenes/DS-DIGI.TTF', 100)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

# ---------------------------------------------------------------------


screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("Pong Hussay")
sonido=pygame.mixer.Sound('sonido/Dinesh-NA-10454_hifi.ogg')

sonido.play(loops=-1)

background_image = pygame.image.load('imagenes/fondo_pong.png')

bola = Bola.Bola(WIDTH,HEIGHT)
pala_jug = Pala.Pala(30,HEIGHT)
pala_cpu = Pala.Pala(WIDTH - 30,HEIGHT)

clock = pygame.time.Clock()

puntos = [0, 0]
while True:
    time = clock.tick(60)
    keys = pygame.key.get_pressed()
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
    puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos,WIDTH,HEIGHT)
    pala_jug.mover(time, keys,HEIGHT)
    pala_cpu.ia(time, bola,WIDTH,HEIGHT)
    p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)
    p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)


    puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos,WIDTH,HEIGHT)
    pala_jug.mover(time, keys,HEIGHT)
    pala_cpu.ia(time, bola,WIDTH,HEIGHT)
    bola.actualizar(time, pala_jug, pala_cpu, puntos,WIDTH,HEIGHT)
    screen.blit(background_image, (0, 0))
    screen.blit(p_jug, p_jug_rect)
    screen.blit(p_cpu, p_cpu_rect)
    screen.blit(bola.image, bola.rect)
    screen.blit(pala_jug.image, pala_jug.rect)
    screen.blit(pala_cpu.image, pala_cpu.rect)
    pygame.display.flip()

