import pygame
pygame.init()
scrin=pygame.display.set_mode((2000, 1000))
fps=pygame.time.Clock()
x=1000
while True:
    fps.tick(80)
    scrin.fill((255, 255, 255))
    pygame.draw.rect(scrin, (192, 192, 192), (750, 485, 500, 50))
    mx=pygame.mouse.get_pos()[0]
    my=pygame.mouse.get_pos()[1]
    
    pygame.draw.circle(scrin, (0, 0, 250), (x, 510), 20)

    bowndbox=pygame.Rect(750, 485, 500, 50)
    
    

    if pygame.mouse.get_pressed()[0]==True and bowndbox.collidepoint(mx, my):
        x=mx
        if x<770:
            x=770
        if x>1230:
            x=1230
        
    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
    
    pygame.display.update()