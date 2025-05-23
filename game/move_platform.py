import pygame
pygame.init() 
import util
import map
import random
import math
import coin

up=True

class Move_platform:
    def __init__(self, x , y, speed_x, speed_y, img):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.img=img
        global up
        if up==True:
            self.timer=0
            up=False
        else:
            self.timer=120
            up=True

    def render(self, scrin, camera_x, camera_y):
        scrin.blit(self.img, (self.x-camera_x, self.y-camera_y))
    def update(self):
        self.timer+=1
        if self.timer<=120:

            self.y+=self.speed_y
        if self.timer>=120:
            self.y+=-self.speed_y
        if self.timer>=240:
            self.timer=0
    def rect(self):
        bowdbox=self.img.get_rect()
        bowdbox.x=self.x
        bowdbox.y=self.y
        return bowdbox
    


    