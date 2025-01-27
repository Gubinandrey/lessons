import pygame
pygame.init()
import os

#загружает одну картинку
def load(file_path, scale):
    file=pygame.image.load(file_path) 
    old_W=file.get_width()
    old_H=file.get_height()
    scale1=pygame.transform.scale(file, (old_W*scale, old_H*scale)).convert_alpha()
    scale1.set_colorkey((0, 0, 0))
    return scale1

#загружает список картинок из папок
def load_images(dirpath,scale):
    n1=[]
    n2=os.listdir(dirpath)
    for asd in n2:
        n3=dirpath+'/'+asd
        n4=load(n3, scale)
        n1.append(n4)
    return n1