import pygame

x1=100
y1=50
W1=300
H1=600

r=90
c_c=96, 96, 96
x2=250
y2=160

c_c1=96, 96, 96
y3=350
c=199


c_c2=96, 96, 96
y4=550
scrin=pygame.display.set_mode((500, 700))
clock=pygame.time.Clock()
while True:
    
    clock.tick(60)
    c+=1
    pygame.draw.rect(scrin, (64, 64, 64), (x1, y1, W1, H1))
    pygame.draw.circle(scrin, c_c, (x2, y2,), r)
    pygame.draw.circle(scrin, c_c1, (x2, y3,), r)
    pygame.draw.circle(scrin, c_c2, (x2, y4,), r)

    

    if c==200:
        c_c=255, 0, 0
        c_c1=96, 96, 96
        c_c2=96, 96, 96
    if c==400:
        c_c=96, 96, 96
        c_c1=255, 153, 51
    if c==550:
        c_c2=0, 255, 0
        c_c=96, 96, 96
        c_c1=96, 96, 96
    if c==700:
        c_c1=255, 153, 51
        c_c2=96, 96, 96
        c=0   


    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)


    pygame.display.update()