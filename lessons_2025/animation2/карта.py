import pygame
pygame.init()
import util

scrin=pygame.display.set_mode((1537, 810))
fps=pygame.time.Clock()

tile_size=32
      
   

tile_map=[[2, 3, 1], [7, 11, 0]]
colors=[[255, 0, 0], [0, 0, 255]]
color=0


while True:
    fps.tick(80)
    scrin.fill((0, 0, 0))
    for asd in tile_map:
        x=asd[0]*tile_size
        y=asd[1]*tile_size
        pygame.draw.rect(scrin, (colors[asd[2]]), (x, y, tile_size, tile_size))
    mx=pygame.mouse.get_pos()[0]
    my=pygame.mouse.get_pos()[1]
    tx=mx//tile_size
    ty=my//tile_size
    pygame.draw.rect(scrin, (128, 128, 128), (tx*tile_size, ty*tile_size, tile_size, tile_size))
    























    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.MOUSEBUTTONDOWN:
            mx=pygame.mouse.get_pos()[0]
            my=pygame.mouse.get_pos()[1]
            tx=mx//tile_size
            ty=my//tile_size
            tile_map.append([tx, ty, color])
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_b:
                color=1
                tile_map.append([tx, ty, color])
            if asd.key==pygame.K_r:
                color=0
                tile_map.append([tx, ty, color])

                

        
        
    pygame.display.update()