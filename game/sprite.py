import pygame
pygame.init()

scrin=pygame.display.set_mode((1535, 810))
fps=pygame.time.Clock()
player=pygame.image.load('C:/Users/andre/программирование пайтон/game/00.png')
w=player.get_width()
h=player.get_height()
player=pygame.transform.scale(player, (10*w, 10*h))
x=100
move_right=False
move_left=False

while True:
    fps.tick(80)
    scrin.fill((0, 0, 0))
    scrin.blit(player, (x, 100))
    if move_right==True:
        x+=10
    if move_left==True:
        x-=10































































    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_d:
                move_right=True
                move_left=False
            if asd.key==pygame.K_a:
                move_right=False
                move_left=True
        if asd.type==pygame.KEYUP:
            if asd.key==pygame.K_d:
                move_right=False
            if asd.key==pygame.K_a:
                move_left=False
    pygame.display.update()