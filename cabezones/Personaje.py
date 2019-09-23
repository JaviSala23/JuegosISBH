#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,pygame
from pygame.locals import *

class Cabeza (pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad, fuerza,imagen,abajo,arriba,derecha,izquierda,patea):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load(imagen)
        self.rectangulo= self.imagen.get_rect()
        self.rectangulo.centerx=x
        self.rectangulo.centery=y
        self.velocidad=velocidad
        self.fuerza=fuerza
        self.arriba=arriba
        self.abajo=abajo
        self.derecha=derecha
        self.izquierda=izquierda
        self.patea=patea

#Fin definicion de atributos
#------------------------------------------
    def mover(self,keys,time,alto,ancho,pelota):


        if self.rectangulo.top>=0:
            if keys[self.arriba]:#Cambiaaar al correspondiente
                self.rectangulo.centery-=self.velocidad*time
                if pelota.colliderect(self.rectangulo):
                    if pelota.top>=0:
                        if self.rectangulo.top <=pelota.bottom and self.rectangulo.centery> pelota.centery :
                            pelota.centery= pelota.centery -0.5*time



        if self.rectangulo.bottom <=alto:
            if keys[self.abajo]:#Cambiaaar al correspondiente
                self.rectangulo.centery+=self.velocidad*time
                if pelota.colliderect(self.rectangulo):
                    if pelota.bottom <=alto:
                        if self.rectangulo.bottom >=pelota.top and self.rectangulo.centery< pelota.centery :
                            pelota.centery= pelota.centery +0.5*time



        if self.rectangulo.right<=ancho-37:
            if keys[self.derecha]:
                self.rectangulo.centerx+=self.velocidad*time
                if pelota.colliderect(self.rectangulo):
                    if pelota.right<=ancho-10:
                        if self.rectangulo.right >=pelota.left and self.rectangulo.centerx< pelota.centerx :
                            pelota.centerx= pelota.centerx +0.5*time


        if self.rectangulo.left>=39:
            if keys[self.izquierda]:
                self.rectangulo.centerx-=self.velocidad*time
                if pelota.colliderect(self.rectangulo):
                    if pelota.left>=10:
                        if self.rectangulo.left <=pelota.right and self.rectangulo.centerx> pelota.centerx :
                            pelota.centerx= pelota.centerx -0.5*time
        
            


    def cabecear (self):
        a=0
        return a
    def colision (self):
        a=0
        return a
    def posInicial (self):
        a=0
        return a


#Definicion de operaciones
#-----------------------------------------
