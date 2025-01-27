import pygame
pygame.init()
import player


scrin=pygame.display.set_mode((1537, 810))
fps=pygame.time.Clock()

player1=player.Player(100, 100, 5)
while True:
    fps.tick(80)
    scrin.fill((0, 255, 128))
    player1.render(scrin)
    player1.update()
    
    































































    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_d:
                player1.move_right=True
                player1.move_left=False
            if asd.key==pygame.K_a:
                player1.move_left=True
                player1.move_right=False
            if asd.key==pygame.K_SPACE:
                player1.speed_y=-15
        if asd.type==pygame.KEYUP:
            if asd.key==pygame.K_d:
                player1.move_right=False
            if asd.key==pygame.K_a:
                player1.move_left=False
        
        
    pygame.display.update()