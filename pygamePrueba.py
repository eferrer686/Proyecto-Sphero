import pygame, sys
from pygame.locals import *

class Sphero(object):
    def __init__(self, posX, posY, vel, MyImage):
        self.posX = posX
        self.posY = posY
        self.vel = vel
        #Imagen
        self.MyImage = MyImage

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def MLeft(object, posX, vel):
            print(posX)
            posX -= vel
            print("posx")
            print(posX)
            print("vel")
            print(vel)

            return posX

    def MRight(object, posX, vel):
            posX += int(vel)

    def MUp(object, posY, vel):
            posY -= int(vel)

    def MDown(object, posY, vel):
            posY += int(vel)

    # if MLeft:
    #     posX -= int(vel)
    #
    # if MRight:
    #     posX += int(vel)
    #
    # if MUp:
    #     posY -= int(vel)
    #
    # if MDown:
    #     posY += int(vel)

class Pared(object):
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY


color = pygame.Color(31, 64, 195)

pygame.init()
#Ventana
venta = pygame.display.set_mode((500, 400))

#Rectangulo
Rectangulo = pygame.Rect(20, 20, 100, 50)

#Color blanco
white = (255, 255, 255)
myImage = pygame.image.load("img/Sphero.png")

pygame.display.set_caption("Laberinto")

#Crear sphero
sphero = Sphero(50, 50, 2, myImage)

while True:
    venta.fill(white)
    venta.blit(sphero.MyImage, (sphero.posX, sphero.posY))
    #pygame.draw.rect(venta, color, Rectangulo, 0)


    for event in pygame.event.get():
        #Cerrar Ventana
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        #Movimiento
        elif(event.type == KEYDOWN):
            if(event.key == K_LEFT):
                sphero.MLeft(sphero.get_posX(), 1)
            if(event.key == K_UP):
                sphero.MUp(sphero.get_posY(), 1)
            if(event.key == K_RIGHT):
                sphero.MRight(sphero.get_posX(), 1)
            elif(event.key == K_DOWN):
                sphero.MDown(sphero.get_posX(), 1)

    pygame.display.update()
