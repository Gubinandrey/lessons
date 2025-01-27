import pygame
pygame.init()
import random
y=100
x=50
speed_x=3
speed_y=3
scrin=pygame.display.set_mode((1200, 800))
clock=pygame.time.Clock()
while True:
    scrin.fill((0, 0, 0))
    pygame.draw.circle(scrin, (170, 0, 130), (x, y), (40))
    x=x+speed_x
    y=y+speed_y
    if x>1160:
        speed_x=-3
        x=x+speed_x
    if x<40:
        speed_x=+3
        x=x+speed_x
    if y>760:
        speed_y=-3
        y=y+speed_y
    if y<40:
        speed_y=+3
        y=y+speed_y
    clock.tick(60)
    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
    pygame.display.update()
    