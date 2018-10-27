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
<<<<<<< HEAD
            self.posX -= vel


    def MRight(self, posX, vel):
            self.posX += int(vel)

    def MUp(self, posY, vel):
            self.posY -= int(vel)

    def MDown(self, posY, vel):
            self.posY += int(vel)

class Pared(object):
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
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()


    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_Height(self):
        return self.Height

    def get_Width(self):
        return self.Width

    def Collide(self, spheroPosX, spheroPosY):
        if(spheroPosX + 25 > self.Xi and spheroPosX - 25 < self.Xf and spheroPosY + 25 > self.Yi and spheroPosY - 25 < self.Yf):
            return True
        else:
            return False
=======
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
>>>>>>> parent of d45f6a8... moveX moveY


color = pygame.Color(31, 64, 195)

<<<<<<< HEAD
#####################################

=======
>>>>>>> parent of d45f6a8... moveX moveY
pygame.init()
#Ventana
venta = pygame.display.set_mode((500, 400))

#Rectangulo
Rectangulo = pygame.Rect(20, 20, 100, 50)

#Color blanco
white = (255, 255, 255)
myImage = pygame.image.load("img/Sphero.png")
pygame.draw.circle(myImage,(0,0,0),(25,25),25,0)

pygame.display.set_caption("Laberinto")

#Crear sphero
sphero = Sphero(50, 50, 2, myImage)
<<<<<<< HEAD
#Crear Pared
pared = Pared(100, 100, 100, 40)
wall = pygame.Rect(pared.get_posX(), pared.get_posY(), pared.get_Width(), pared.get_Height())
=======
>>>>>>> parent of d45f6a8... moveX moveY

while True:
    venta.fill(white)
    venta.blit(sphero.MyImage, (sphero.posX, sphero.posY))
    #Dibujar Pared
    venta.blit(pared.surf, (pared.posX, pared.posY))
    
    #pygame.draw.Rect(venta, color, wall, 0)
    #pygame.draw.rect(venta, color, Rectangulo, 0)


    for event in pygame.event.get():
        #Cerrar Ventana
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        #Movimiento
        elif(event.type == KEYDOWN):
            if(event.key == K_LEFT):
<<<<<<< HEAD
                sphero.MLeft(sphero.get_posX(), 1)
=======
                print(str(sphero.get_posX()) + "PosX antes")
                sphero.MLeft(sphero.get_posX(), 1)
                print(str(sphero.get_posX()) + "Pos despues")
>>>>>>> parent of d45f6a8... moveX moveY
            if(event.key == K_UP):
                sphero.MUp(sphero.get_posY(), 1)
            if(event.key == K_RIGHT):
                sphero.MRight(sphero.get_posX(), 1)
            elif(event.key == K_DOWN):
                sphero.MDown(sphero.get_posX(), 1)

    pygame.display.update()
