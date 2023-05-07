import pygame
import random
from Entity import *
#initializing the arrays containing all things related to the entities and their images
level=1
things=[]

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
#initializing the player and appending it to the arrays
player=Entity(250,250,r"C:\Users\user\source\repos\OOPGame\OOPGame\other\gunslinger.png",screen)
things.append(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    for thing in things:
        thing.printIt()
    #screen.blit(things[0].image,(player.x_coor , player.y_coor))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y_coor -= 300 * dt
    if keys[pygame.K_s]:
        player.y_coor += 300 * dt
    if keys[pygame.K_a]:
        player.x_coor -= 300 * dt
    if keys[pygame.K_d]:
        player.x_coor += 300 * dt
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()