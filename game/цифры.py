import pygame
import random
scrin=pygame.display.set_mode((500, 550))
fps=pygame.time.Clock()



Rect_1x=200
Rect_1y=200
W1=70
H1=20
c1=64, 64, 64

Rect_2x=Rect_1x+W1
Rect_2y=Rect_1y+H1
W2=20
H2=70
c2=64, 64, 64


Rect_3x=Rect_1x-H1
Rect_3y=Rect_1y+H1
W3=20
H3=70
c3=64, 64, 64

Rect_4x=200
Rect_4y=Rect_3y+H3
W4=70
H4=20
c4=64, 64, 64

Rect_5x=Rect_2x
Rect_5y=Rect_4y+H4
W5=20
H5=70
c5=64, 64, 64 

Rect_6x=Rect_3x
Rect_6y=Rect_5y
W6=20
H6=70
c6=64, 64, 64

Rect_7x=200
Rect_7y=Rect_6y+H6
W7=70
H7=20
c7=64, 64, 64
while True:
    fps.tick(60)
    scrin.fill((0, 0, 0))
    pygame.draw.rect(scrin, c1, (Rect_1x, Rect_1y, W1, H1))
    pygame.draw.rect(scrin, c2, (Rect_2x, Rect_2y, W2, H2))
    pygame.draw.rect(scrin, c3, (Rect_3x, Rect_3y, W3, H3))
    pygame.draw.rect(scrin, c4, (Rect_4x, Rect_4y, W4, H4))
    pygame.draw.rect(scrin, c5, (Rect_5x, Rect_5y, W5, H5))
    pygame.draw.rect(scrin, c6, (Rect_6x, Rect_6y, W6, H6))
    pygame.draw.rect(scrin, c7, (Rect_7x, Rect_7y, W7, H7))

    for asd in pygame.event.get():  
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_1:
                c1=64, 64, 64
                c2=0, 255, 128
                c3=64, 64, 64
                c4=64, 64, 64
                c5=0, 255, 128
                c6=64, 64, 64
                c7=64, 64, 64
            if asd.key==pygame.K_2:
                c1=0, 255, 128
                c2=0, 255, 128
                c3=64, 64, 64
                c4=0, 255, 128
                c5=64, 64, 64
                c6=0, 255, 128
                c7=0, 255, 128
            if asd.key==pygame.K_3:
                c1=0, 255, 128
                c2=0, 255, 128
                c3=64, 64, 64
                c4=0, 255, 128
                c5=0, 255, 128
                c6=64, 64, 64
                c7=0, 255, 128
            if asd.key==pygame.K_4:
                c1=64, 64, 64
                c3=0, 255, 128
                c4=0, 255, 128
                c2=0, 255, 128
                c5=0, 255, 128
                c6=64, 64, 64
                c7=64, 64, 64
            if asd.key==pygame.K_5:
                c1=0, 255, 128
                c2=64, 64, 64
                c3=0, 255, 128
                c4=0, 255, 128
                c5=0, 255, 128
                c6=64, 64, 64
                c7=0, 255, 128
            if asd.key==pygame.K_6:
                c1=0, 255, 128
                c2=64, 64, 64
                c3=0, 255, 128
                c4=0, 255, 128
                c5=0, 255, 128
                c6=0, 255, 128
                c7=0, 255, 128
            if asd.key==pygame.K_7:
                c1=0, 255, 128
                c2=0, 255, 128
                c3=64, 64, 64
                c4=64, 64, 64
                c5=0, 255, 128
                c6=64, 64, 64
                c7=64, 64, 64
            if asd.key==pygame.K_8:
                c1=0, 255, 128
                c2=0, 255, 128
                c3=0, 255, 128
                c4=0, 255, 128
                c5=0, 255, 128
                c6=0, 255, 128
                c7=0, 255, 128
            if asd.key==pygame.K_9:
                c1=0, 255, 128
                c2=0, 255, 128
                c3=0, 255, 128
                c4=0, 255, 128
                c5=0, 255, 128
                c6=64, 64, 64
                c7=0, 255, 128
            if asd.key==pygame.K_0:
                c1=0, 255, 128
                c2=0, 255, 128
                c3=0, 255, 128
                c4=64, 64, 64
                c5=0, 255, 128
                c6=0, 255, 128
                c7=0, 255, 128
    pygame.display.update()
    