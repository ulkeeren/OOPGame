import pygame
import random
from Entity import *
zombieTimer=0
xrandom=random.seed(420)
yrandom=random.seed(69)
zombieCounter=0
zombies=[]
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
time_passed=0
running = True
dt = 0
#initializing the player and appending it to the arrays
player=Gunslinger(250,250,r"C:\Users\user\source\repos\OOPGame\OOPGame\other\gunslinger.png",screen)
while running:
    zombieTimer+=dt
    if zombieTimer>2:
        zombies.append(Zombie(random.randint(0,1280),random.randint(0,720),r"C:\Users\user\source\repos\OOPGame\OOPGame\other\zomb.png",screen))
        zombieTimer=0
    time_passed+=clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    mousePressed=pygame.mouse.get_pressed()
    mousePos=pygame.mouse.get_pos()
    if any(mousePressed) and time_passed>1:
        player.shoot_bullet(mousePos[0],mousePos[1])
        time_passed=0
    keys = pygame.key.get_pressed()
    player.update(keys,dt)
    player.printIt()
    for zombie in zombies:
        player.checkBulletCollision(zombie)
        zombie.update(player.x_coor,player.y_coor,dt)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    time_passed+=dt

pygame.quit()