import pygame
pygame.init()
import os

scrin=pygame.display.set_mode((1537, 810))
fps=pygame.time.Clock()
n1=[]
for asd in range(0, 5):
    file_path=f'C:/Users/andre/программирование пайтон/lessons_2025/animation2/explosion/exp{asd}.png'
    file=pygame.image.load(file_path)
    old_W=file.get_width()
    old_H=file.get_height()
    scale=6
    scale1=pygame.transform.scale(file, (old_W*scale, old_H*scale))
    n1.append(scale1)
index=0
timer=0
while True:
    fps.tick(80)
    scrin.fill((0, 0, 0))
    timer+=1
    if timer==10:
        index+=1
        timer=0
    if index>=5:
        index=0
    scrin.blit(n1[index], (500, 150))
    
    
    
    































































    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
        
    pygame.display.update()