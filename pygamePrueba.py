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

    def get_vel(self):
        return self.vel

    def MLeft(self, posX, vel):
            # print(posX)
            posX -= vel
            # print("posx")
            # print(posX)
            # print("vel")
            # print(vel)

    def MRight(self, posX, vel):
            posX += int(vel)

    def MUp(self, posY, vel):
            posY -= int(vel)

    def MDown(self, posY, vel):
            posY += int(vel)

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
                print(str(sphero.get_posX()) + "PosX antes")
                sphero.MLeft(sphero.get_posX(), 1)
                print(str(sphero.get_posX()) + "Pos despues")
            if(event.key == K_UP):
                sphero.MUp(sphero.get_posY(), 1)
            if(event.key == K_RIGHT):
                sphero.MRight(sphero.get_posX(), 1)
            elif(event.key == K_DOWN):
                sphero.MDown(sphero.get_posX(), 1)

    pygame.display.update()
