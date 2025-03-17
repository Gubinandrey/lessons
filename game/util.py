import pygame
import os




def load(file_name, scale):
    img=pygame.image.load(file_name).convert_alpha()
    w=img.get_width()
    h=img.get_height()
    new_img=pygame.transform.scale(img, (w*scale, h*scale)).convert_alpha()
    new_img.set_colorkey((0, 0, 0))
    return new_img 





def load_img(file_road, scale):
    file_names=sorted(os.listdir(file_road))
    sorted1=(file_names)
    n1=[]
    for asd in sorted1:
        picture=load(file_road+'/'+asd, scale)
        n1.append(picture)
    return n1