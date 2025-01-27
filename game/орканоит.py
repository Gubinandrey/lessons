import pygame
import random
pygame.init()
scrin=pygame.display.set_mode((1000, 600))
music1=pygame.mixer.Sound('game/defeat.mp3')
music2=pygame.mixer.Sound('game/win.mp3')
max_circle_speed=3




def generate_colour():
    first_colour=random.randint(0, 255)
    second_colour=random.randint(0, 255)
    third_colour=random.randint(0, 255)
    return [first_colour, second_colour, third_colour]

        
class Rect:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.colour=generate_colour()
        self.speed=random.randint(3, 4)
        self.rect_move_left=False
        self.rect_move_right=False
    def render(self):
        pygame.draw.rect(scrin, self.colour, (self.x, self.y, 80, 10))
    def update(self):
        
        if self.x<0:
            self.rect_move_right=True
            self.rect_move_left=False
        if self.x+80>1000:
            self.rect_move_right=False
            self.rect_move_left=True
        
        
        if self.rect_move_left==True:
            self.x=self.x-self.speed
        if self.rect_move_right==True:
            self.x=self.x+self.speed
    def npc(self):
        for asd in rects:
            bowndbox_asd=pygame.Rect(asd.x, asd.y, 80, 10)
            bowndbox_self=pygame.Rect(self.x, self.y, 80, 10)
            if self!=asd:
                if bowndbox_self.colliderect(bowndbox_asd):

                    if self.rect_move_right==True:
                        self.rect_move_right=False
                        self.rect_move_left=True
                    elif self.rect_move_left==True:
                        self.rect_move_right=True
                        self.rect_move_left=False
platform=Rect(460, 580)       




class Ball:
    def __init__(self):
        self.x=500
        self.y=300
        self.radius=10
        self.x_speed=random.randint(-max_circle_speed, max_circle_speed)
        self.y_speed=random.randint(-max_circle_speed, max_circle_speed)
        self.colour=255, 0, 0
        if self.x_speed==0:
            self.x_speed=1
        if self.y_speed==0:
            self.y_speed=1
    def render(self):
        pygame.draw.circle(scrin, self.colour, (self.x, self.y), self.radius)
    def update(self):
        self.x=self.x+self.x_speed
        self.y=self.y+self.y_speed
        if self.x-self.radius<0:
            self.x_speed=-self.x_speed
        if self.x+self.radius>1000:
            self.x_speed=-self.x_speed
        if self.y-self.radius<0:
            self.y_speed=-self.y_speed
        
        bowndbox_ball=pygame.Rect(self.x-self.radius, self.y-self.radius, 2*self.radius, 2*self.radius)
        bowndbox_platform=pygame.Rect(platform.x, platform.y, 80, 10)
        for asd in rects:
            asd_bowndbox=pygame.Rect(asd.x, asd.y, 80, 10)
            if asd_bowndbox.colliderect(bowndbox_ball):
                rects.remove(asd)
        if bowndbox_ball.colliderect(bowndbox_platform):
            self.y_speed=-self.y_speed
        
font=pygame.font.SysFont('Futura', (270))
font1=pygame.font.SysFont('Futura', (245))
payza=False
ball=Ball()
rects=[]
fps=pygame.time.Clock()
for asd in range(0, 1001-160, 160):
    for aqws in range(0, 151, 10):
        rectasd=Rect(asd, aqws)
        rects.append(rectasd)
        rectasd.rect_move_right=True
    
while True:
    fps.tick(120)
    if payza==False:
        scrin.fill((0, 0, 0))   
        
        for awsd in rects:
            awsd.npc()
            awsd.render()
            awsd.update()
            
        ball.render()
        ball.update()
        
        platform.render()
        platform.update()
        for asd in pygame.event.get():
            if asd.type==pygame.KEYDOWN:
                if asd.key==pygame.K_RIGHT:
                    platform.rect_move_right=True
                    platform.rect_move_left=False
                if asd.key==pygame.K_LEFT:
                    platform.rect_move_right=False
                    platform.rect_move_left=True
                if asd.key==pygame.K_ESCAPE:
                    payza=True
                    pygame.display.set_caption('ПАУЗА')
            if asd.type==pygame.QUIT:
                exit(0)
        if len(rects)==0:
            bot_text3=font.render(str('YOU'), True, (255, 0, 0))
            bot_text4=font.render(str('WIN'), True, (255, 0, 0))
            scrin.blit(bot_text3, (230, 60))
            scrin.blit(bot_text4, (275, 300))
            music2.play()
        bot_text1=font.render(str('GAME'), True, (255, 0, 0))
        bot_text2=font1.render(str('OVER'), True, (255, 0, 0))
        if ball.y>600:
            scrin.blit(bot_text1, (230, 60))
            scrin.blit(bot_text2, (275, 300))
            music1.play()
        pygame.display.update()
    else: 
        for asd in pygame.event.get():
            if asd.type==pygame.QUIT:
                exit(0)
            if asd.type==pygame.KEYDOWN:
                if asd.key==pygame.K_ESCAPE:
                    payza=False
                    pygame.display.set_caption('ИГРА')