import pygame
pygame.init()
import random
import math
class Particle:
    def __init__(self, x, y, color):
        self.speed_x=1
        self.speed=random.randint(5, 11)
        self.x=x
        self.y=y
        self.colors=color
        self.r=random.randint(1, 4)
        self.timer=0
        self.engle=(random.random()-0.5)*4*math.pi
        self.speed_x=self.speed*math.cos(self.engle)
        self.speed_y=self.speed*math.sin(self.engle)
        self.timer=random.randint(10, 38)
        
    def update(self):
        self.timer-=1
        self.x+=self.speed_x
        self.y+=self.speed_y
    def render(self, scrin, mapic):
        pygame.draw.circle(scrin, self.colors, (self.x-mapic.camera_x, self.y-mapic.camera_y), self.r)

class Coin:
    def __init__(self, x, y, color):
        self.x=x
        self.y=y
        self.color=color
        self.c_bbx=pygame.Rect(self.x-25, self.y+16*3-25, 50, 50)
        self.particles=[]
        for asd in range(15):
            self.particles.append(Particle(self.x, self.y+16*3+30, (153, 153, 0)))
    def render(self, scrin, mapic):
        pygame.draw.circle(scrin, (self.color), (self.x-mapic.camera_x, self.y-mapic.camera_y+16*3), 25)
        for asd in self.particles:
            asd.render(scrin, mapic)
    def update(self):
        for asd in self.particles:
            asd.update()
            if asd.timer<0:
                self.particles.remove(asd)
        if random.randint(0, 15)==6:
            self.particles.append(Particle(self.x, self.y+16*3, (153, 153, 0)))
        
        