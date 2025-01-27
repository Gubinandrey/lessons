import pygame
import random
scrin=pygame.display.set_mode((1000, 600))
fps=pygame.time.Clock()
Rect_2x=200
Rect_2y=200
Rect_1x=200
W2=200
H2=200

brx=200
bry=200
Wbr=200
hbr=200











left_colour=255, 0, 0
right_colour=255, 0, 0
Rect_1y=200
W1=200
H1=200
while True:
    fps.tick(60)
    scrin.fill((0, 0, 0))
    pygame.draw.rect(scrin, left_colour, (Rect_1x, Rect_1y, W2, H2))
    pygame.draw.rect(scrin, right_colour, (Rect_1x+W1+200, Rect_2y, W2, H2))
    for asd in pygame.event.get():  
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_a:
                left_colour=0, 0, 255
                right_colour=255, 0, 0
            if asd.key==pygame.K_d:
                left_colour=255, 0, 0
                right_colour=0, 0, 255
            if asd.key==pygame.K_SPACE:
                left_colour=255, 0, 0
                right_colour=255, 0, 0
    pygame.display.update()
         


        
    