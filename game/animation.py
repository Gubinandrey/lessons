import pygame
pygame.init()
import util


class Animation:
    def __init__(self, files_path, scale):
        self.images=util.load_img(files_path, scale)
        self.index=0
        self.timer=8
    def update(self):
        self.timer-=1
        if self.timer==0:
            self.index+=1
            if self.index==len(self.images):
                self.index=0
            self.timer=8
    def render(self, scrin, x, y, flip):
        self.image=self.images[self.index]
        if flip==True:
            self.image=pygame.transform.flip(self.image, True, False).convert_alpha()
            self.image.set_colorkey((0, 0, 0))
        scrin.blit(self.image, (x, y))
    def get_height(self):
        self.now_index=self.images[self.index]
        return self.now_index.get_height()
    def get_now_img(self):
        return self.images[self.index]
    def reset(self):
        self.timer=8
        self.index=0