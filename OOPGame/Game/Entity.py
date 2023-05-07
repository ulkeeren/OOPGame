from asyncio.windows_events import NULL
from math import sqrt
from tkinter.font import NORMAL
import pygame
class Entity:
    screen=NULL
    x_coor=NULL
    y_coor=NULL
    image=NULL
    rect=NULL
    def __init__(self,x_coor,y_coor,image_path,screen):
        self.x_coor=x_coor
        self.y_coor=y_coor
        self.image=pygame.image.load(image_path)
        self.screen=screen
    def printIt(self):
        self.screen.blit(self.image,(self.x_coor,self.y_coor))
    def getRect(self):
        return self.image.get_rect()
class Gunslinger(Entity):
    def __init__(self,x_coor,y_coor,image_path,screen):
        super().__init__(x_coor,y_coor,image_path,screen)
        self.image=pygame.transform.scale(self.image,(100,90))
    bullets=[]
    magsize=6

    class Bullet():
        #where bullet is going to move every frame
        dx=NULL
        dy=NULL
        #initial position, player position
        px=NULL
        py=NULL
        image=NULL
        screen=NULL
        def __init__(self,dx,dy,px,py,screen):
            self.dx=dx
            self.dy=dy
            self.px=px
            self.py=py
            self.cpx=px
            self.cpy=py
            self.screen=screen
            self.image=pygame.transform.scale(pygame.image.load(r"C:\Users\user\source\repos\OOPGame\OOPGame\other\bullet.png"),(10,10))
        def update(self,dt):
            xwide=(self.dx-self.px)
            ywide=(self.dy-self.py)
            normalization=sqrt((xwide**2) + (ywide**2))
            self.cpx+=((self.dx-self.px)/normalization)*1200*dt
            self.cpy+=((self.dy-self.py)/normalization)*1200*dt
        def checkCollision(self,zomb):
            if pygame.Rect((self.cpx,self.cpy),(10,10)).colliderect(pygame.Rect((zomb.x_coor,zomb.y_coor),(100,90))):
                zomb.dead=True
        def printIt(self):
            self.screen.blit(self.image,(self.cpx,self.cpy))
     
    def shoot_bullet(self,dx,dy):
        self.bullets.append(self.Bullet(dx,dy,self.x_coor,self.y_coor,self.screen))
        if dx>self.x_coor:
            pygame.transform.flip(self.image,False,True)
    def checkBulletCollision(self,zomb):
        for bullet in self.bullets:
            bullet.checkCollision(zomb)
    def update(self,keys,dt):
        if keys[pygame.K_w]:
           self.y_coor -= 300 * dt
        if keys[pygame.K_s]:
           self.y_coor += 300 * dt
        if keys[pygame.K_a]:
           self.x_coor -= 300 * dt
        if keys[pygame.K_d]:
           self.x_coor += 300 * dt
        for bullet in self.bullets:
            bullet.printIt()
            bullet.update(dt)
class Zombie(Entity):
    def __init__(self,x_coor,y_coor,image_path,screen):
        super().__init__(x_coor,y_coor,image_path,screen)
        self.image=pygame.transform.scale(self.image,(100,90))
    dead=False
    def update(self,px,py,dt):
        if not self.dead:
            xwide=(self.x_coor-px)
            ywide=(self.y_coor-py)
            normalization=sqrt((xwide**2) + (ywide**2))
            self.x_coor-=((self.x_coor-px)/normalization)*300*dt
            self.y_coor-=((self.y_coor-py)/normalization)*300*dt
        else:
            pygame.transform.rotate(self.image,90)
        self.printIt()