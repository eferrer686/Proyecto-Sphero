import pygame, sys
from pygame.locals import *

from classes import Meta,Sphero

HEIGHT_WINDOW = 400
WIDTH_WINDOW = 500
metaX = 450
metaY = 350


color = pygame.Color(31, 64, 195)

#Incia Juego
pygame.init()
#Ventana
venta = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))

#Rectangulo
Rectangulo = pygame.Rect(20, 20, 100, 50)

#Color blanco
white = (255, 255, 255)
myImage = pygame.image.load("img/Sphero.png")
pygame.display.set_caption("Laberinto")

#Crear sphero
spheros = []
#Reset al simulador con nueva generacion

def resetSim(gen):
    print("Generacion: " + str(gen))
    #Dummy BestSphero
    bestSphero = Sphero(50, 50, 1, myImage,WIDTH_WINDOW,HEIGHT_WINDOW,metaX,metaY)
    
    #Get best sphero
    if len(spheros) > 0:
        bestSphero = spheros[0]
        bestScore = bestSphero.score

        for sphero in spheros:

            sphero.setScore()
            print("Sphero score: " + str(sphero.score))

            if sphero.score >= bestScore:
                bestSphero.destroy()
                bestSphero = sphero
                bestScore = sphero.score
            else:
                sphero.destroy()

        print("Best Score: " + str(bestScore))

    spheros.clear()
    
    bestSphero.posX = 50
    bestSphero.posY = 50
    spheros.append(bestSphero)

    for n in range(4):
        tempSphero = Sphero(50, 50, 1, myImage,WIDTH_WINDOW,HEIGHT_WINDOW,metaX,metaY)
        tempSphero.brain.copy(bestSphero.brain)
        tempSphero.brain.mutate()
        spheros.append(tempSphero)

#Meta
meta = Meta(metaX, metaY, 50, 50)

#Evento timeout
RESETSIM = USEREVENT +1
pygame.time.set_timer(RESETSIM, 15000)

gen = 0
resetSim(gen)

running = True





while running:

    venta.fill(white)

    venta.blit(meta.surf, (meta.posX, meta.posY))
    pygame.draw.rect(venta, (0,255,0), meta.rect)

    for sphero in spheros:
        venta.blit(sphero.MyImage, (sphero.posX, sphero.posY))
        sphero.move()
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == RESETSIM:
            gen +=1
            resetSim(gen)
        # Check for QUIT event; if QUIT, set running to false
        if event.type == QUIT:
            running = False
    
