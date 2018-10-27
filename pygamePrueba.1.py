import pygame, sys
from pygame.locals import *

import rnn

HEIGHT_WINDOW = 400
WIDTH_WINDOW = 500
###Clase Sphero
class Sphero(object):
    def __init__(self, posX, posY, vel, MyImage):
        self.posX = posX
        self.posY = posY
        self.vel = vel
        #Imagen
        self.MyImage = MyImage
        self.brain = rnn.Brain(4,8,4)
        self.metaX = 450
        self.metaY = 350


    def move(self):
        print(self.posX)
        print(self.posY)
        moveArray = self.brain.predict([[self.posX/500,self.posY/400,self.metaX,self.metaY]]) 
        print(moveArray)

        if moveArray[0,0] > 0.5 :
            self.MRight(self.vel)
        if moveArray[0,1] > 0.5 :
            self.MLeft(self.vel)
        if moveArray[0,2] > 0.5 :
            self.MUp(self.vel)
        if moveArray[0,3] > 0.5 :
            self.MDown(self.vel)
        

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_vel(self):
        return self.vel

    def MLeft(self, vel):
        if(sphero.posX >= 0):
            self.posX -= vel
    def MRight(self, vel):
        if(sphero.posX <= 500):
            self.posX += vel
    def MUp(self, vel):
        if (sphero.posY >= 0):
            self.posY -= vel
    def MDown(self, vel):
        if(sphero.posY <= 400):
            self.posY += vel

    def MoveX(self,vel):
        self.posX += vel
    def MoveY(self,vel):
        self.posY +=vel

color = pygame.Color(31, 64, 195)

#Rectangulo
Rectangulo = pygame.Rect(20, 20, 100, 50)

#Color blanco
white = (255, 255, 255)
myImage = pygame.image.load("img/Sphero.png")

pygame.display.set_caption("Laberinto")

#Crear sphero
sphero = Sphero(50, 50, 2, myImage)
moveRight = True
moveDown = True
while True:
    sphero.move()