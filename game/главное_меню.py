import pygame
import random
import time
pygame.init()
import util


class Main_menu:
    def __init__(self):
        self.bg=util.load('/Users/andrey/python/lessons/game/images/icons_menu/background.jpg', 0.8)
        self.bg.set_colorkey((255, 255, 255))
        self.shift=0
        self.play_button=Button(0.35, 750, 425, '/Users/andrey/python/lessons/game/images/icons_menu/play_button-no-bg-preview (carve.photos).png')
        self.select_menu=Level_sekect_menu()
    def run(self, scrin, fps, next_level, start, run ):
        pygame.event.clear()

        while True:
            fps.tick(80)
            scrin.fill((255, 255, 255))
            

            scrin.blit(self.bg, (self.shift, 0))
            scrin.blit(self.bg, (self.shift-self.bg.get_width(), 0))
            self.play_button.update()
            
            self.play_button.render(scrin)   
            for asd in pygame.event.get():
                if asd.type==pygame.QUIT:
                    exit(0)
                if asd.type==pygame.MOUSEBUTTONDOWN and self.play_button.hower==True:
                    
                    self.select_menu.run(scrin, fps, next_level, start, run)
            pygame.display.flip()
class Button:
    def __init__(self, scale, x, y, file_path):
        self.buttons=util.load(file_path, scale)
        self.bbx_button=pygame.Rect(x, y, self.buttons.get_width(), self.buttons.get_height())
        self.hower=False
    def update(self):
        
        if self.bbx_button.collidepoint(pygame.mouse.get_pos()):
            self.hower=True
            pygame.display.set_caption('wdsnmvbc dmnav mjwa')

            
        else:
            self.hower=False
    def render(self, scrin):
        scrin.blit(self.buttons, (self.bbx_button.x, self.bbx_button.y))

class Level_sekect_menu:
    def __init__(self):
        self.bg=util.load('/Users/andrey/python/lessons/game/images/icons_menu/background_select_level.jpg', 1.1)
        self.bg.set_colorkey((255, 255, 255))
        self.shift=0
        
        self.how_many_levels=2
        self.color_start=[197, 20, 7]
        self.color_end=[252, 40, 0]
        self.color_digit_start=[255, 255, 255]
        self.color_digit_end=[51, 255, 255]
        self.color_digit=[255, 255, 255]
        self.period=160
        #self.timer=0
        self.color=[197, 20, 7]
        self.now_coctounie=True
        self.clic=False
        
        self.digit_font=pygame.font.Font(None, 100)
    def run(self, scrin, fps, next_level, start, run):
        pygame.event.clear()

        
        while True:
            fps.tick(80)
            
            
            self.render(scrin, fps)
            self.update(scrin, next_level, start, run, fps)
            
            self.clic=False
            for asd in pygame.event.get():
                if asd.type==pygame.QUIT:
                    exit(0)
                if asd.type==pygame.MOUSEBUTTONDOWN:
                    self.clic=True
            
    def render(self, scrin, fps):
        scrin.fill((255, 255, 255))
        scrin.blit(self.bg, (self.shift, 0))
        self.scrin_2=pygame.Surface((2050, 1025), (pygame.SRCALPHA))
        self.scrin_2.fill((255, 255, 255, 0))
        x=250
        y=300 
        #if self.timer<self.period:
        if self.now_coctounie==True:
            self.color[0]+=0.34375
            self.color[1]+=0.125
            self.color[2]+=-0.04375
            self.color_digit[0]-=1.275
            if self.color[0]>252:
                self.now_coctounie=False
            if self.color[1]>40:
                self.now_coctounie=False
            if self.color[2]<0:
                self.now_coctounie=False
        else:
            if self.now_coctounie==False:
                self.color[0]-=0.34375
                self.color[1]-=0.125
                self.color[2]-=-0.04375
                self.color_digit[0]+=1.175
                if self.color[0]<197:
                    self.now_coctounie=True
                if self.color[1]<20:
                    self.now_coctounie=True
                if self.color[2]>7:
                    self.now_coctounie=True
        
        self.now_level_digit=1

        for asd in range(3):
            for awsd in range(5):
                self.digit_img_now_level=self.digit_font.render(str(self.now_level_digit), True, (self.color_digit))
                self.bbx_buttons=pygame.Rect(x-60, y-60, 120, 120)
                if self.bbx_buttons.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(self.scrin_2, (192, 192, 192, 210), (x, y), 60)
                else:
                    pygame.draw.circle(self.scrin_2, self.color, (x, y), 60)

                
                if self.now_level_digit>9:
                    self.scrin_2.blit(self.digit_img_now_level, (x-40, y-30))
                else:
                    self.scrin_2.blit(self.digit_img_now_level, (x-20, y-30))
                self.now_level_digit+=1
                
                x+=380
                
            y+=283.333333333333333333333333
            x=250
        scrin.blit(self.scrin_2, (0, 0))
      
        pygame.display.flip()
    def update(self, scrin, next_level, start, run, fps ):
        self.x=250
        self.y=300
    
        for asd in range(3):
            for awsd in range(5):
                self.bbx_buttons=pygame.Rect(self.x-60, self.y-60, 120, 120)
                pygame.draw.rect(scrin, (0, 0, 255), (self.x, self.y, 120, 120))
                if self.bbx_buttons.collidepoint(pygame.mouse.get_pos())and self.clic==True:
                    start_menu=Start_menu_map()
                    start_menu.run(scrin, next_level, start, run, fps, self.run)
                    
                else:
                    self.clic=False
                
                    
                self.x+=380
                
            self.y+=283.333333333333333333333333
            self.x=250
                    

                






class Start_menu_map:
    def __init__(self ):
        self.background_LeVel_menu=util.load('/Users/andrey/python/lessons/game/images/icons_menu/start_LeVel_menu.jpg', 1.3)
        self.play_button_start_menu_map=Button(0.75, 1350, 425, '/Users/andrey/python/lessons/game/images/icons_menu/play_button_start_menu1.png') 
        self.play_button_start_menu_map_bbx=self.play_button_start_menu_map.bbx_button
        self.home_button=Button(0.24, 1370, 600, '/Users/andrey/python/lessons/game/images/icons_menu/home_button_to_play.png')
        self.back_button_in_Start_menu_map_menu=Button(0.498, 1360, 280, '/Users/andrey/python/lessons/game/images/icons_menu/back_button_in_Start_menu_map_menu.png')
    def render(self, scrin):
        scrin.blit(self.background_LeVel_menu, (508.85, 200))
        
    def run(self, scrin, next_level, start, run, fps, run_2):
        pygame.event.clear()
        
        while True:
            self.render(scrin)
            self.play_button_start_menu_map.render(scrin)
            self.back_button_in_Start_menu_map_menu.render(scrin)
            self.home_button.render(scrin)
            if self.play_button_start_menu_map_bbx.collidepoint(pygame.mouse.get_pos())and pygame.mouse.get_pressed()[0]==True:
                next_level()
                start()
            self.back_button_in_Start_menu_map_menu_bbx=self.back_button_in_Start_menu_map_menu.bbx_button
            self.home_button_bbx=self.home_button.bbx_button
            if self.home_button_bbx.collidepoint(pygame.mouse.get_pos())and pygame.mouse.get_pressed()[0]==True:
                run(scrin, fps, next_level, start, run)
            if self.back_button_in_Start_menu_map_menu_bbx.collidepoint(pygame.mouse.get_pos())and pygame.mouse.get_pressed()[0]==True:
                run_2( scrin, fps, next_level, start, run)
            for asd in pygame.event.get():
                if asd.type==pygame.QUIT:
                    exit(0)
            pygame.display.update()