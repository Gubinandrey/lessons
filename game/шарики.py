import pygame
pygame.init()
import util
import random


scrin=pygame.display.set_mode((2050, 1050))
fps=pygame.time.Clock()

class Ball:
    def __init__(self):
        self.color=random.randint(0, 255)
        self.randomx=random.randint(10, 2000)
        self.randomy=random.randint(10, 1000)
        self.radius=10
        self.balls={}
    def render(self):
        for awsd in range(0, 21):
            for asd in self.balls:
                pygame.draw.circle(scrin, (self.color, self.color, self.color), (self.randomx, self.randomy), self.radius)

        


ball=Ball()
while True:
    fps.tick(80)
    scrin.fill((102, 255, 255))
    ball.render()
    #ball.update()


    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)


    pygame.display.update()