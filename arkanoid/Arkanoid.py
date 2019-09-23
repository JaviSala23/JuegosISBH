#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
import Bola
import Pala
import Ladrillo
import Mapa

# Constantes
WIDTH = 605
HEIGHT = 480
fuente = pygame.font.Font(None, 100)
final=pygame.image.load("imagenes/fin.png")


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ARKANOID Hussay")
    #variables
    punto=0
    pop= pygame.mixer.Sound("sonido/pop.wav")
    pala=Pala.Pala(WIDTH,HEIGHT)
    bola = Bola.Bola(WIDTH,HEIGHT)

#MAPA.................ARKANOID



    mapa1=Mapa.mapa()
    ladrillos=mapa1.mapa1()




    clock = pygame.time.Clock()

    vidas = 5
    juego=True
    pygame.mixer.music.load("sonido/Beat-1.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    while juego==True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        a=bola.actualizar(time,WIDTH,HEIGHT,pala)
        vidas=vidas-a
        pala.mover(time,keys,WIDTH)
        a=0
        ladri=len(ladrillos)
        for lista in range(ladri):
            punt=ladrillos[a].colision(bola,time)
            a=a+1
            punto=punto+punt

        if vidas<=0:
            gameover = fuente.render("GAME OVER", 0, (0, 0, 0))
            screen.blit(gameover, (100,160))
        elif punto==ladri*100:
            pantalla.fill ((255,255,255))  
            gameover = fuente.render("GANASTE", 0, (0, 0, 0))
            screen.blit(gameover, (100,160))

        else:
            screen.fill((255,255,255))
            screen.blit(bola.image,bola.rect)
            screen.blit(pala.image,pala.rect)
            b=0
            for ac in range(ladri):
                screen.blit(ladrillos[b].image,ladrillos[b].rect)
                b=b+1




        pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    main()
