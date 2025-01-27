import pygame
import random
pygame.init()
scrin=pygame.display.set_mode((1000, 600))
fps=pygame.time.Clock()
rect_x1=10
rect_y1=260
speed_y1=4
rect_W1=10
rect_H1=100
rect_move_up1=False
rect_move_down1=False



rect_W2=10
rect_x2=990-rect_W2
rect_y2=260
speed_y2=4
rect_H2=100
rect_move_up2=False
rect_move_down2=False

max_circle_speed=5
radius=40
circle_x=500
circle_y=300
circle_x_speed=random.randint(-max_circle_speed, max_circle_speed)
circle_y_speed=random.randint(-max_circle_speed, max_circle_speed)
while True:
    scrin.fill((0, 0, 0))
    if rect_move_up1==True:
        rect_y1=rect_y1-speed_y1
    if rect_move_down1==True:
        rect_y1=rect_y1+speed_y1
    if rect_y1+rect_H1>600:
        rect_y1=600-rect_H1
    if rect_y1<0:
        rect_y1=0
    pygame.draw.rect(scrin, (0,250, 5), (rect_x1, rect_y1, rect_W1, rect_H1))   

    circle_x=circle_x+circle_x_speed
    circle_y=circle_y+circle_y_speed
    if circle_x-radius<0:
        circle_x=500
        circle_y=300
        circle_x_speed=random.randint(-max_circle_speed, max_circle_speed)
        circle_y_speed=random.randint(-max_circle_speed, max_circle_speed)
    if circle_x-radius>1000:
        circle_x=500
        circle_y=300
        circle_x_speed=random.randint(-max_circle_speed, max_circle_speed)
        circle_y_speed=random.randint(-max_circle_speed, max_circle_speed)
    if circle_y-radius<0:
        circle_y=radius
        circle_y_speed=-circle_y_speed
    if circle_y+radius>600:
        circle_y=600-radius
        circle_y_speed=-circle_y_speed
    pygame.draw.circle(scrin, (250, 0, 5), (circle_x, circle_y), (radius))

    if rect_move_up2==True:
        rect_y2=rect_y2-speed_y2
    if rect_move_down2==True:
        rect_y2=rect_y2+speed_y2
    if rect_y2+rect_H2>600:
        rect_y2=600-rect_H2
    if rect_y2<0:
        rect_y2=0
    pygame.draw.rect(scrin, (0,250, 5), (rect_x2, rect_y2, rect_W2, rect_H2))
    


    
    fps.tick(60)
    for asd in pygame.event.get():
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_UP:
                rect_move_down1=False
                rect_move_up1=True
            if asd.key==pygame.K_DOWN:
                rect_move_down1=True
                rect_move_up1=False
        if asd.type==pygame.QUIT:
            exit(0)
    pygame.display.update()
