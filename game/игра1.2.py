import pygame
pygame.init()
import random
scrin=pygame.display.set_mode((1200, 800))
clock=pygame.time.Clock()
y=100
x=50
speed_x=random.randint(1, 50)
speed_y=random.randint(1, 50)
while True:
    scrin.fill((0, 0, 0))
    pygame.draw.circle(scrin, (170, 0, 130), (x, y), (40))
    x=x+speed_x
    y=y+speed_y
    if x>1160:
        speed_x=-random.randint(1, 10)
        x=x+speed_x
    if x<40:
        speed_x=random.randint(1, 10)
        x=x+speed_x
    if y>760:
        speed_y=-random.randint(1, 10)
        y=y+speed_y
    if y<40:
        speed_y=random.randint(1, 10)
        y=y+speed_y
    clock.tick(60)
    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
    pygame.display.update()