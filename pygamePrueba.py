import pygame, sys
from pygame.locals import *
HEIGHT_WINDOW = 400
WIDTH_WINDOW = 500

###Clase Sphero
class Sphero(object):
    def __init__(self, posX, posY, vel, MyImage, walls):
        self.posX = posX
        self.posY = posY
        self.vel = vel
        #Paredes
        self.walls = walls

        #Imagen
        self.MyImage = MyImage
    def get_posX(self):
        return self.posX
    def get_posY(self):
        return self.posY
    def get_vel(self):
        return self.vel
    def MLeft(self, vel):
        isCollisioning = False
        for item in walls:
            if(item.rect.colliderect(self)):
                isCollisioning = True
        if(isCollisioning == False):
            self.posX -= (vel)
    def MRight(self, vel):
        isCollisioning = False
        for item in walls:
            if(item.rect.colliderect(self)):
                isCollisioning = True
        if(isCollisioning == False):
            self.posX += (vel)
    def MoveX(self,vel):
        isCollisioning = False
        for item in walls:
            if(item.rect.colliderect(self)):
                isCollisioning = True
        if(isCollisioning == False):
            self.posX += vel
    def MoveY(self,vel):
        isCollisioning = False
        for item in walls:
            if(item.rect.colliderect(self)):
                isCollisioning = True
        if(isCollisioning == False):
            self.posY +=vel
    def MUp(self, vel):
        isCollisioning = False
        for item in walls:
            if(item.rect.colliderect(self)):
                isCollisioning = True
        if(isCollisioning == False):
            self.posY -= (vel)

    def MDown(self, vel):
        isCollisioning = False
        for item in walls:
            if(item.rect.colliderect(self)):
                isCollisioning = True
        if(isCollisioning == False):
            self.posY += (vel)

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
sphero = Sphero(50, 50, 2, myImage,[])
moveRight = True
moveDown = True
while True:
    venta.fill(white)
    venta.blit(sphero.MyImage, (sphero.posX, sphero.posY))
    #pygame.draw.rect(venta, color, Rectangulo, 0)
    ##Eje X
    if(sphero.posX<=50 and moveRight != True):
        moveRight = True
    elif(sphero.posX>=WIDTH_WINDOW-50 and moveRight == True):
        moveRight = False
    direccionX = 1 if(moveRight) else -1
    sphero.MoveX(direccionX)
    ##Eje Y
    if(sphero.posY<=50 and moveDown != True):
        moveDown = True
    elif(sphero.posY>=HEIGHT_WINDOW-50 and moveDown == True):
        moveDown = False
    direccionY = 1 if(moveDown) else -1
    sphero.MoveY(direccionY)


    pygame.display.update()
