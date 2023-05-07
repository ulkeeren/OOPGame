from asyncio.windows_events import NULL
import pygame
class Entity:
    screen=NULL
    x_coor=NULL
    y_coor=NULL
    image=NULL
    def __init__(self,x_coor,y_coor,image_path,screen):
        self.x_coor=x_coor
        self.y_coor=y_coor
        self.image=pygame.transform.scale(pygame.image.load(image_path),(160,147))
        self.screen=screen
    rect=pygame.Rect(x_coor,y_coor,160,147)
    def printIt(self):
        self.screen.blit(self.image,(self.x_coor,self.y_coor)).convert()
class Gunslinger(Entity):
    def __init__(self,x_coor,y_coor):
        super().__init__(self,x_coor,y_coor)

    bullets=[]
    magsize=6

    class Bullet():
        #where bullet is going to move every frame
        dx=NULL
        dy=NULL
        #initial position, player position
        px=NULL
        py=NULL

        image=pygame.image.load("C:\Users\user\source\repos\OOPGame\OOPGame\other\bullet.png").convert()
        screen=NULL
        def __init__(self,dx,dy,px,py,screen):
            self.dx=dx
            self.dy=dy
            self.px=px
            self.py=py
            self.screen=screen
        def update(self,dt):
            self.px=(self.dx-self.px)*dt
            self.py=(self.dy-self.py)*dt
        def checkCollision(self):
            pass
        def printIt(self):
            self.screen.blit(self.image,(self.px,self.py))
    def shoot_bullet(self,dx,dy):
        self.bullets.append(self.Bullet(dx,dy,self.x_coor,self.y_coor,self.screen))
    def checkBulletCollision(self):
        for bullet in self.bullets:
            bullet.checkCollision()