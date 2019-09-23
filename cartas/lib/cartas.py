import pygame
class Carta: 
    def __int__  (self, img,grupo,coor,escala,tapada,destapada,estado):  
        self.img=img
        self.estado=estado
        self.grupo=grupo
        self.coor=coor 
        self.escala=escala
        self.tapada=tapada
        self.destapada=destapada
    def tapar(self):
        self.img=pygame.image.load(self.tapada)
        self.img=pygame.transform.smoothscale(self.img, self.escala)
    def destapar(self):
        self.img=pygame.image.load(self.destapada)
        self.img=pygame.transform.smoothscale(self.img, self.escala)
        self.estado=2