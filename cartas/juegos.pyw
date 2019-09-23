import pygame
import random
import time
import datetime
from lib.cartas import *
#iniciar libreria Pyagame
pygame.init()

#colores
blueclaro=	(242, 229, 128)
negro=(0,0,0)
#fondo = pygame.image.load("fondo").convert()
#pantalla.blit(fondo, (0, 0))
fuente = pygame.font.Font(None, 25)
final=pygame.image.load("img/fin.png")


#lista de imagenes de cartas
tapada="img/cartas/tapada.png"
cartas=[("img/cartas/cartaa.png","img/cartas/cartaaaa.png"),
("img/cartas/cartab.png","img/cartas/cartabb.png"),
("img/cartas/cartac.png","img/cartas/cartacc.png"),
("img/cartas/cartad.png","img/cartas/cartadd.png"),
("img/cartas/cartae.png","img/cartas/cartaee.png"),
("img/cartas/cartaf.png","img/cartas/cartaff.png"),
("img/cartas/cartag.png","img/cartas/cartagg.png"),
("img/cartas/cartah.png","img/cartas/cartahh.png"),
("img/cartas/cartai.png","img/cartas/cartaii.png"),
("img/cartas/cartaj.png","img/cartas/cartajj.png"),
("img/cartas/cartak.png","img/cartas/cartakk.png"),
("img/cartas/cartal.png","img/cartas/cartall.png"),
("img/cartas/cartam.png","img/cartas/cartamm.png"),
("img/cartas/cartan.png","img/cartas/cartann.png"),
("img/cartas/cartañ.png","img/cartas/cartaññ.png"),
("img/cartas/cartao.png","img/cartas/cartaoo.png"),
("img/cartas/cartap.png","img/cartas/cartapp.png"),
("img/cartas/cartaq.png","img/cartas/cartaqq.png"),
("img/cartas/cartar.png","img/cartas/cartarr.png"),
("img/cartas/cartas.png","img/cartas/cartass.png"),
("img/cartas/cartat.png","img/cartas/cartatt.png"),
("img/cartas/cartau.png","img/cartas/cartauu.png"),
("img/cartas/cartav.png","img/cartas/cartavv.png"),
("img/cartas/cartaw.png","img/cartas/cartaww.png"),
("img/cartas/cartax.png","img/cartas/cartaxx.png"),
("img/cartas/cartay.png","img/cartas/cartayy.png"),
("img/cartas/cartaz.png","img/cartas/cartazz.png")]
coor= [(50,30),(180,30),(310,30),(440,30),(570,30),
(50,160),(180,160),(310,160),(440,160),(570,160),
(50,290),(180,290),(310,290),(440,290),(570,290),
(50,420),(180,420),(310,420),(440,420),(570,420)]
juego=[]
#cambiar la cantidad de cartas
j=26
x=19
#x=int(input("cargar la dificultad"))

dif=(x+1)/2
dif=int(dif)

for i in range (0,dif):
    #creamos dos objetso de la clase carta
    c_objeto=Carta()
    c1_objeto=Carta()
    #generamos las imagens aleatorias
    c=random.randint(0,j)
    #cargamos las imagenes a los objetos
    c_objeto.destapada=cartas[c][0]
    c1_objeto.destapada=cartas[c][1]
    c_objeto.tapada=tapada
    c1_objeto.tapada=tapada
    c_objeto.estado=1
    c1_objeto.estado=1

    c_objeto.escala=(120,120)
    c1_objeto.escala=(120,120)
    c_objeto.tapar()
    c1_objeto.tapar()
    
    c_objeto.grupo= i
    c1_objeto.grupo=i
    cartas.pop(c)

    #generamos las coordenadas aleatorias para la carta uno
    cor1=random.randint(0,x)
    c_objeto.coor=coor[cor1]
    coor.pop(cor1)
     #generamos las coordenadas aleatorias para la carta 2
    cor2=random.randint(0,x-1)
    c1_objeto.coor=coor[cor2]
    coor.pop(cor2)
    #agregamos a la lista juegos objetos, c1 yc2 contienen
    #los datos de las crtas seleccionada aleatoria
    juego.append((c_objeto,c1_objeto))

    j=j-1
    x=x-2

#dimension pantalla
dimension=(750,550)
pantalla=pygame.display.set_mode(dimension)
pygame.display.set_caption("Juego de los Pares")
error_sonido= pygame.mixer.Sound("sound/error.wav")
correcto_sonido= pygame.mixer.Sound("sound/win.wav")
a=True
pause = False



comparacion=[]
concar=0
intento=0
fallidos=0
correcto=0
musica_juego='sound/juego.wav'
musica_ganador='sound/ganaste.mp3'
#intermos hasta que a== True
class musica:
    def __init__(self,musica_juego,musica_ganador,tipo):
        self.juego=musica_juego
        self.ganador=musica_ganador
        self.tipo=tipo
    
    def play(self):
        if self.tipo==1:  
            pygame.mixer.music.load(self.juego)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load(musica_ganador)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)

musica_so=musica(musica_juego,musica_ganador,1)  
musica_so.play()



while a==True:
    
    

    
    for il in range (0,dif):
        for ih in range (0,2):
            if juego[il][ih].estado==2:
               
                if len(comparacion)!=0:
                    
                    if juego[il][ih].img!=comparacion[0].img:
                        comparacion.append(juego[il][ih])
                        concar=concar+1
                        
                        
                        
                        
                        if concar==2:
                            intento=intento+1
                            
                            if comparacion[0].grupo==comparacion[1].grupo:
                                pygame.mixer.Sound.play(correcto_sonido)
                                comparacion[0].estado=3
                                comparacion[1].estado=3
                                comparacion=[]
                                correcto=correcto+1

                                concar=0
                               

                            else:
                                
                                pygame.mixer.Sound.play(error_sonido)
                                comparacion[0].estado=1
                                comparacion[1].estado=1
                                comparacion[0].tapar()
                                comparacion[1].tapar()
                                comparacion=[]
                                concar=0
                                fallidos=fallidos+1
            
                
                 

    
#para cuando el usuario desea realizar una accion 
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            a= False

    #captura si hacemos clic
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # toma las coordenadas en donde hice clic

            x1, y = evento.pos
            #recorre lista juegos en l, y h recorre la tupla de la misma
            for l in range (0,dif):
                for h in range (0,2):
                    # crea un rectangulo de colicion del tamaño de la carta

                    carta1=juego[l][h].img.get_rect()
                    #mueve el rectangulo a las coordenadas de las carta
                    carta1=carta1.move(juego[l][h].coor)
                    if carta1.collidepoint(x1, y):
                        if juego[l][h].estado==1:
                            juego[l][h].destapar()
                            comparacion.append(juego[l][h])




    pantalla.fill (blueclaro)  
    cjuegos=[]
    for i in range (0,dif):
        pantalla.blit(juego[i][0].img,juego[i][0].coor)
        pantalla.blit(juego[i][1].img,juego[i][1].coor)
       

                    


    
    texto = fuente.render("Intentos: " + str(intento)+"  Fallidos: "+str(fallidos)+"  Correctos: " + str(correcto) , True, negro)  
    pantalla.blit(texto, [150, 10])
    if correcto==dif:
        if musica_so.tipo==1:
            musica_so.tipo=2
            musica_so.play()
        pantalla.fill (blueclaro)  
        pantalla.blit(final,(0,0))
        texto = fuente.render("Intentos: " + str(intento)+"  Fallidos: "+str(fallidos)+"  Correctos: " + str(correcto) , True, negro)  
        ganador=fuente.render("ganaste",True, negro)
        pantalla.blit(texto ,[200,25])
    pygame.display.flip()  
   


pygame.quit()
