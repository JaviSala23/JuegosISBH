#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importamos pygame:
import pygame
from pygame.locals import *
# Importación para las imágenes:
import Pelota
import Personaje
import Arco
import sys, os
#import ConfigParser
# Importación para fuentes de pygame, y da un error si no funciona:
#if not pygame.font: print "No funcionan las fuentes de pygame."
# Importación para reproducir sonidos en pygame, y da un error si no funciona:
#if not pygame.mixer: print "No funciona el sonido de pygame."
pygame.mixer.init()
sonido = pygame.mixer.Sound('sonido.ogg')
sonido.play(loops=-1)


#...........................cierre de importaciones de modulos
pygame.init()

#Variables
WIDTH = 1000
HEIGHT= 500

fondos= ["Fondo\CanchaVerde.png","Fondo\CanchaAzul.png"]
fondo1= pygame.image.load(fondos[0])
personajes= ["Imagenes\personaje1.png","Imagenes\personaje2.png","Imagenes\personaje3.png","Imagenes\personaje4.png"]
# Definición principal del programa:

def main():
        # Crea la ventana:
        fuente = pygame.font.Font(None, 300)
        fuente2 = pygame.font.Font(None, 70)
        cont1= 0
        cont2= 0
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Cabezones 1.0")
        arcoIzq=Arco.Arco(38,HEIGHT/2)
        arcoDer=Arco.Arco(WIDTH-38,HEIGHT/2)
        arcoDer.imagen=pygame.transform.flip(arcoDer.imagen,True,False)
        personaje1=Personaje.Cabeza(900,210,0.5,0.5,personajes[0],K_DOWN,K_UP,K_RIGHT,K_LEFT,K_RCTRL)
        personaje2=Personaje.Cabeza(100,210,0.5,0.5,personajes[1],K_s,K_w,K_d,K_a,K_c)
        personaje2.imagen=pygame.transform.flip(personaje2.imagen,True,False)
        
        pelota1=Pelota.Pelota(WIDTH/2,HEIGHT/2,0.5)
        clock=pygame.time.Clock()
        a = True

        while a==True:
            time=clock.tick(60)
            keys = pygame.key.get_pressed()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            personaje1.mover( keys,time, HEIGHT, WIDTH,pelota1.rectangulo)
            personaje2.mover( keys,time, HEIGHT, WIDTH,pelota1.rectangulo)

#validar Gol--------------------------------------------------------
            if pelota1.rectangulo.centerx < 30:
                if pelota1.rectangulo.top > arcoDer.rectangulo.top:
                    if pelota1.rectangulo.bottom< arcoDer.rectangulo.bottom:
                        cont1=cont1+1
                        
                        pelota1.rectangulo.centerx=WIDTH/2
                        pelota1.rectangulo.centery=HEIGHT/2
            if pelota1.rectangulo.centerx > WIDTH-30:
                if pelota1.rectangulo.top > arcoDer.rectangulo.top:
                    if pelota1.rectangulo.bottom< arcoDer.rectangulo.bottom:
                        cont2=cont2+1
                        
                        pelota1.rectangulo.centerx=WIDTH/2
                        pelota1.rectangulo.centery=HEIGHT/2
#Validar Afuera.------------------------------------------------------
            if pelota1.rectangulo.left <7:
                pelota1.rectangulo.centerx=WIDTH/2
                pelota1.rectangulo.centery=HEIGHT/2
            if pelota1.rectangulo.right> WIDTH-7:
                pelota1.rectangulo.centerx=WIDTH/2
                pelota1.rectangulo.centery=HEIGHT/2

            gol1 = fuente.render(str(cont1), 0, (255, 255, 255))
            gol2 = fuente.render(str(cont2), 0, (255, 255, 255))
            ganador1 = fuente2.render("EL Jugador 1 es el Ganador", 0, (255, 255, 255))
            ganador2 = fuente2.render("EL Jugador 2 es el Ganador", 0, (255, 255, 255))

            if cont1==10:
                screen.blit(ganador1, (200,180))
                screen.blit(gol1, (WIDTH-400,HEIGHT/2))
                screen.blit(gol2, (280,HEIGHT/2))
            elif cont2==10:
                screen.blit(ganador2, (200,180))
                screen.blit(gol1, (WIDTH-400,HEIGHT/2))
                screen.blit(gol2, (280,HEIGHT/2))
            else:
        #actualiza objeto screen

                screen.blit(fondo1,(0,0))
                screen.blit(gol1, (WIDTH-400,HEIGHT/2))
                screen.blit(gol2, (280,HEIGHT/2))
                screen.blit(pelota1.imagen, pelota1.rectangulo)
                screen.blit(personaje1.imagen, personaje1.rectangulo)
                screen.blit(personaje2.imagen, personaje2.rectangulo)
                screen.blit(arcoIzq.imagen, arcoIzq.rectangulo)
                screen.blit(arcoDer.imagen, arcoDer.rectangulo)




        # Imprimimos los cambios en la pantalla:
            pygame.display.flip()
            pygame.display.update()
            screen.blit(fondo1,(0,0))


# Comienza el juego:
if __name__ == "__main__":
    pygame.init()
    main()
