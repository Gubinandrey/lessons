import pygame
import os
def load(file_name, scale):
    img=pygame.image.load(file_name)
    w=img.get_width()
    h=img.get_height()
    new_img=pygame.transform.scale(img, (w*scale, h*scale))
    return new_img 
def load_img(file_road, scale):
    file_names=os.listdir(file_road)
    sorted1=sorted(file_names)
    n1=[]
    for asd in sorted1:
        picture=load(file_road+'/'+asd, scale)
        n1.append(picture)
    return n1