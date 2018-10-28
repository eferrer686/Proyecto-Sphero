import pygame
import rnn
import math

#Globals
HEIGHT_WINDOW = 400
WIDTH_WINDOW = 500
metaX = 450
metaY = 350

##Class Meta
class Meta(object):
    def __init__(self, posX, posY, Height, Width):
        self.Width = Width
        self.Height = Height
        self.posX = posX
        self.posY = posY
        self.Xi = self.posX - (self.Width/2)
        self.Xf = self.posX + (self.Width/2)
        self.Yi = self.posY - (self.Height/2)
        self.Yf = self.posY + (self.Height/2)
        self.surf = pygame.Surface((self.Width, self.Height))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY



    def Collide(self, spheroPosX, spheroPosY):
        if(spheroPosX + 25 > self.Xi and spheroPosX - 25 < self.Xf and spheroPosY + 25 > self.Yi and spheroPosY - 25 < self.Yf):
            return True
        else:
            return False

##Class Sphero
class Sphero(object):
    def __init__(self, posX, posY, vel, MyImage,WIDTH_WINDOW,HEIGHT_WINDOW,metaX,metaY):
        self.posX = posX
        self.posY = posY

        self.vel = vel

        #Imagen
        self.MyImage = MyImage

        self.WIDTH_WINDOW = WIDTH_WINDOW
        self.HEIGHT_WINDOW = HEIGHT_WINDOW

        self.brain = rnn.Brain(3,1,4)
        
        self.metaX = metaX
        self.metaY = metaY

        
        #Distancia a la meta
        self.sX = self.posX + self.metaX
        self.sY = self.posY + self.metaY
        self.dist = math.sqrt(math.pow(self.sX,2)+math.pow(self.sY,2))

        self.score = -1000

    def destroy(self):
        self.brain.destroy()
        del self

    def getDist(self):
        sX = self.posX + self.metaX
        sY = self.posY + self.metaY
        
        return math.sqrt(math.pow(self.sX,2)+math.pow(self.sY,2))

    def move(self):
        nX = self.posX/WIDTH_WINDOW
        nY = self.posY/HEIGHT_WINDOW

        dist = self.getDist()      
        
        moveArray = self.brain.predict([[nX,nY,dist]]) 

        if moveArray[0,0] > 0.5 :
            self.moveRight(self.vel)
        if moveArray[0,1] > 0.5 :
            self.moveLeft(self.vel)
        if moveArray[0,2] > 0.5 :
            self.moveUp(self.vel)
        if moveArray[0,3] > 0.5 :
            self.moveDown(self.vel)

    def moveLeft(self, vel):
        if(self.posX > 0):
            self.posX -= vel
    def moveRight(self, vel):
        if(self.posX < WIDTH_WINDOW-50):
            self.posX += vel
    def moveUp(self, vel):
        if (self.posY > 0):
            self.posY -= vel
    def moveDown(self, vel):
        if(self.posY < HEIGHT_WINDOW-50):
            self.posY += vel

    def setScore(self):
        sX = self.posX + self.metaX
        sY = self.posY + self.metaY
        self.score = math.sqrt(math.pow(sX,2)+math.pow(sY,2)) - self.dist\
    