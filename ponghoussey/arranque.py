#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Módulos
import sys, pygame
from pygame.locals import *



# Constantes
WIDTH = 640
HEIGHT = 480
pygame.init()
# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
pygame.mixer.init()
sonido = pygame.mixer.Sound('sonido/Beat-1.ogg')
sonido.play(loops=-1)
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
# Cargar la imagen del flecha

# Variable que controla la posición de Guy

#almacenamos las difrentes imagenes en un dicionario
mario={}
posicionx=[260,190,125,60]
posiciony=[139,175,210,250]

#variable que controla que imagenb del hombre se muestra
cual=0
cualx=0
cualy=0
#controlador del tiempo
cuanto =80
tiempo=0
# ---------------------------------------------------------------------

def main():
        global cualx,cualy, posicionx,posiciony,personaje
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Smash Houssay")

        background_image = load_image('imagenes/eseariointro.png')
        while True:
                for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
        # Modificar posición en función de la tecla pulsada
                teclasPulsadas = pygame.key.get_pressed()
                if teclasPulsadas[K_1]:
                    pygame.quit()
                    import juego
                elif teclasPulsadas[K_2]:
                    pygame.quit()
                    import juego
                elif teclasPulsadas[K_ESCAPE]:
                        pygame.quit()
                        sys.exit()
# Dibujar el fondo de color
                screen.fill((0,0,0))
                screen.blit(background_image, (0, 0))
                pygame.display.flip()
                pygame.display.update()


if __name__ == '__main__':
        pygame.init()
        main()
