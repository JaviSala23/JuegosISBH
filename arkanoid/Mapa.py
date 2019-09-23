#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
import Ladrillo
from pygame.locals import *
pygame.init()

class mapa():

    def mapa1(self):
        mapa=[]
        la=-1
        anc=60
        x=33
        y=0
        for a in range (4):
            y=y+33
            x=33
            la=la+1
            for b in range(10):

                mapa.append(Ladrillo.Ladrillo(la,x,y))
                x=x+anc

        return mapa