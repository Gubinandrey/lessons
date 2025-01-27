import pygame
import random
pygame.init()
scrin=pygame.display.set_mode((1000, 600))
fps=pygame.time.Clock()
rect_x1=4
rect_y1=260
speed_y1=4
rect_W1=10
rect_H1=100
rect_move_up1=False
rect_move_down1=False
rect_W2=10
rect_x2=990-rect_W2
rect_y2=260
speed_y2=2
rect_H2=100
rect_move_up2=False
rect_move_down2=False
max_circle_speed=5
radius=30
speed=1
circle_x=500
circle_y=300
circle_x_speed=random.randint(-max_circle_speed, max_circle_speed)
circle_y_speed=random.randint(-max_circle_speed, max_circle_speed)
guest_wins=0
bot_wins=0
chiter=False
font=pygame.font.SysFont('Futura', (60))
payza=False
while True: 
    if payza==False:
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
        if chiter==False:
            if rect_move_up2==True:
                rect_y2=rect_y2-speed_y2
            if rect_move_down2==True:
                rect_y2=rect_y2+speed_y2
            if rect_y2+rect_H2>600:
                rect_y2=600-rect_H2
            if rect_y2<0:
                rect_y2=0
            pygame.draw.rect(scrin, (0,250, 5), (rect_x1, rect_y1, rect_W1, rect_H1))  
            circle_x=circle_x+circle_x_speed
            circle_y=circle_y+circle_y_speed
            bowndbox=pygame.Rect(circle_x-radius, circle_y-radius, 2*radius, 2*radius)
            left_Rect=pygame.Rect(rect_x1, rect_y1, rect_W1, rect_H1)
            right_Rect=pygame.Rect(rect_x2, rect_y2, rect_W2, rect_H2)
            if bowndbox.colliderect(left_Rect):
                circle_x=rect_x1+rect_W1+radius
                circle_x_speed=-circle_x_speed
                circle_x_speed=circle_x_speed+circle_x_speed
                circle_y_speed=circle_y_speed+circle_y_speed
            if bowndbox.colliderect(right_Rect):
                circle_x=rect_x2-radius
                circle_x_speed=-circle_x_speed
                circle_x_speed=circle_x_speed+circle_x_speed
                circle_y_speed=circle_y_speed+circle_y_speed
            if circle_x-radius<0:
                circle_x=500
                circle_y=300
                circle_x_speed=random.randint(-max_circle_speed, max_circle_speed)
                circle_y_speed=random.randint(-max_circle_speed, max_circle_speed)
                bot_wins+=+1
            if circle_x-radius>1000:
                circle_x=500
                circle_y=300
                circle_x_speed=random.randint(-max_circle_speed, max_circle_speed)
                circle_y_speed=random.randint(-max_circle_speed, max_circle_speed)
                guest_wins+=1
            if circle_y-radius<0:
                circle_y=radius
                circle_y_speed=-circle_y_speed
            if circle_y+radius>600:
                circle_y=600-radius
                circle_y_speed=-circle_y_speed
            if rect_move_up2==True:
                rect_y2=rect_y2-speed_y2
            if rect_move_down2==True:
                rect_y2=rect_y2+speed_y2
            if rect_y2+rect_H2>600:
                rect_y2=600-rect_H2
            if rect_y2<0:
                rect_y2=0            
            d_y=(rect_x2-circle_x)/circle_x_speed*circle_y_speed   
            y_intr=circle_y+d_y
            if y_intr<rect_y2:
                rect_move_up2=True
                rect_move_down2=False
            if y_intr>rect_y2+rect_H2:
                rect_move_down2=True
                rect_move_up2=False
        pygame.draw.circle(scrin, (250, 0, 5), (circle_x, circle_y), (radius))
        pygame.draw.rect(scrin, (0,250, 5), (rect_x2, rect_y2, rect_W2, rect_H2))
        pygame.draw.rect(scrin, (0,250, 5), (rect_x1, rect_y1, rect_W1, rect_H1))
    fps.tick(60)
    for asd in pygame.event.get():
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_UP:
                rect_move_down1=False
                rect_move_up1=True
            if asd.key==pygame.K_ESCAPE:
                if payza==False:
                    payza=True
                else:
                    payza=False
            if asd.key==pygame.K_SPACE:
                if chiter==False:
                    chiter=True
                else:
                    chiter=False
            if asd.key==pygame.K_g:
                circle_x=500
                circle_y=300
            if asd.key==pygame.K_DOWN:
                rect_move_down1=True
                rect_move_up1=False
        if asd.type==pygame.QUIT:
            exit(0) 
    if payza==False:
        guest_text=font.render(str(guest_wins), True, (255, 255, 0))
        bot_text=font.render(str(bot_wins), True, (255, 255, 0))
        scrin.blit(guest_text, (4,5))
        scrin.blit(bot_text, (971,5))      
        pygame.display.update()