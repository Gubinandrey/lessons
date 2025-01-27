import pygame
pygame.init()
import animation1
import physics



class Player:
    def __init__(self, x, y, scale):
        self.x=x
        self.y=y
        self.anim=animation1.Animation('C:/Users/andre/программирование пайтон/game/images/entities/player/run', 5)
        self.speed=4
        self.move_left=False
        self.move_right=False
        self.flip=False
        self.speed_y=0
    def update(self):
        print('start', self.speed_y)
        if self.move_right==True:
            self.x+=self.speed
            self.flip=False
        if self.move_left==True:
            self.x-=self.speed
            self.flip=True
        self.anim.update()
        self.speed_y+=physics.graviti
        self.y+=self.speed_y
        print('end', self.speed_y)
        if self.y>=physics.ground-self.anim.get_height():
            self.y=physics.ground-self.anim.get_height()
    def render(self, scrin):
        self.anim.render(scrin, self.x, self.y, self.flip)
    

        