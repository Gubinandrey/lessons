import pygame
import util
class Animation:
    def __init__(self, file_road, scale):
        self.imges=util.load_img(file_road, scale)
        self.now_index=0
    def update(self):
        self.now_index+=1
        if self.now_index==len(self.imges):
            self.now_index=0
    def get_now_img(self):
        return self.imges[self.now_index]