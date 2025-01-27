import pygame
pygame.init()
import util

scrin=pygame.display.set_mode((1537, 810))
fps=pygame.time.Clock()
class Tile_map:
    def __init__(self):
        self.tile_size=32
        self.tile_map={
            (10, 13):{
                'type':'grass', 
                'index':0
            }

        }
        self.resource={
            'grass':util.load_images('C:/Users/andre/программирование пайтон/game/images/tiles/grass', 2)

        }
    def render(self):
        for asd in self.tile_map:
            desk=self.tile_map[asd]
            x=asd[0]*self.tile_size
            y=asd[1]*self.tile_size
            image=self.resource[desk['type']][desk['index']]
            scrin.blit(image, (x, y))
    def update(self):
        self.mx=pygame.mouse.get_pos()[0]
        self.my=pygame.mouse.get_pos()[1]
        self.tx=self.mx//self.tile_size
        self.ty=self.my//self.tile_size
        self.tile_map[(self.tx, self.ty)]={
                'type':'grass', 
                'index':0}
map=Tile_map()

while True:
    fps.tick(80)
    scrin.fill((0, 0, 0))
    map.render()
    























    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.MOUSEBUTTONDOWN:
            map.update()

        
        
    pygame.display.update()