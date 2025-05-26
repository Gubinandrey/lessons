import pygame
pygame.init() 
import util
import time
import animation
import map
import random
import platform
import math
import coin
import главное_меню
import move_platform
min_dist=2050
pygame.mixer.init()
if platform.system()=='Darwin':
    W =2050
    H =1050
    BASE_DIR = '/Users/andrey/python/lessons/game'
else:
    W, H = 800, 600
    BASE_DIR = 'game'

level=3
scrin=pygame.display.set_mode((W, H))
mapic=map.Tile_map(scrin, 3)
pula_music=pygame.mixer.Sound(f'{BASE_DIR}/sfx/выстрел.mp3')
pula_music.set_volume(0.3)
jump_music=pygame.mixer.Sound(f'{BASE_DIR}/sfx/jump.wav')
hit_music=pygame.mixer.Sound(f'{BASE_DIR}/sfx/hit.wav')
font=pygame.font.SysFont('Ura Bum Bum SP', 120)
fps=pygame.time.Clock()
projectile=util.load(f'{BASE_DIR}/images/projectile.png', mapic.k-0.2)
gravition=.5
sparksssss=[]
projectiles=[]
scrinshake=0
shrink=0
scrin_2=pygame.Surface((W, H), pygame.SRCALPHA)
expand=0
local={
'zelia_double_jump':True,
'no_perezaradka':True

}
all={
'zelia_double_jump':3,
'no_perezaradka':3


}


class Player:
    def __init__(self, x, y, enemy):
        self.x=x
        self.y=y
        self.change_gun_timer=240
        self.my_coins=0
        self.pula_timer=30
        self.fire_timer=30
        self.xp=100
        mapic.k=7
        self.many_pules=0
        self.дробовик_3000=util.load(f'{BASE_DIR}/images/дробовик_для_игры_обрезанный_3000.png', mapic.k/20, False)
        self.дробовик_3000_bbx=self.дробовик_3000.get_rect()
        self.gun=util.load(f'{BASE_DIR}/images/gun.png', mapic.k+1)
        self.оружки=self.gun, self.дробовик_3000
        self.now_оружка=self.оружки[0]
        
        
        if enemy==False:
            self.animationsss={
                'idle': animation.Animation(f'{map.BASE_DIR}/images/entities/player/idle', mapic.k+2),
                'run': animation.Animation(f'{map.BASE_DIR}/images/entities/player/run', mapic.k+2),
                'jump': animation.Animation(f'{map.BASE_DIR}/images/entities/player/jump', mapic.k+2)
            }
        if enemy==True:
            self.animationsss={
                'idle': animation.Animation(f'{map.BASE_DIR}/images/entities/enemy/idle', mapic.k+2),
                'run': animation.Animation(f'{map.BASE_DIR}/images/entities/enemy/run', mapic.k+2),
                'jump': animation.Animation(f'{map.BASE_DIR}/images/entities/enemy/idle', mapic.k+2),

            }
        self.current='idle'
        self.move_right=False
        self.move_left=False
        self.speed_x=6
        self.speed_y=0
        self.flip=False
        self.timer=120
        self.jumps=0
        #self.sprite=self.animation.get_now_img()
        
       
    def render(self):
        img=pygame.transform.flip(self.animationsss[self.current].get_now_img(), self.flip, False)
        
        img.set_colorkey((0, 0, 0))
    
        scrin.blit(img, (self.x-mapic.camera_x-self.rect().width/4, self.y-mapic.camera_y))
        if self.flip==False:
            if self.оружки[0]==self.now_оружка:
                self.now_оружка.set_colorkey((0, 0, 0))
                scrin.blit(self.now_оружка, (self.rect().right-mapic.camera_x, self.rect().centery-mapic.camera_y))
            if self.оружки[1]==self.now_оружка:
                scrin.blit(self.now_оружка, (self.rect().right-20-mapic.camera_x, self.rect().centery-5-mapic.camera_y))
            
        else:
            gunimg=pygame.transform.flip(self.now_оружка, True, False)
            if self.оружки[0]==self.now_оружка:
                gunimg.set_colorkey((0, 0, 0))
                scrin.blit(gunimg, (self.rect().left-12-mapic.camera_x, self.rect().centery-mapic.camera_y))
            if self.оружки[1]==self.now_оружка:
                scrin.blit(gunimg, (self.rect().left-70-mapic.camera_x, self.rect().centery-5-mapic.camera_y))

        for asd in projectiles:
            asd.render()
        pygame.draw.rect(scrin, (255, 0, 0), (self.x-mapic.camera_x, self.y-mapic.camera_y, 60, 10))
        pygame.draw.rect(scrin, (0, 255, 0), (self.x-mapic.camera_x, self.y-mapic.camera_y, 60*self.xp/100, 10))
        if self==player:
            pygame.draw.circle(scrin, (204, 204, 0), (70, 70), 40 )
            self.text=font.render(str(self.my_coins), True, (0, 0, 0))
            scrin.blit(self.text, (135, 38))
    def rect(self):
        img=self.animationsss[self.current].get_now_img()
        bowdbox=img.get_rect()
        bowdbox.x=self.x
        bowdbox.y=self.y
        self.new_bbx=pygame.Rect(self.x, self.y, bowdbox.width/2, bowdbox.height)
        return self.new_bbx
    def update(self):
        self.rect()
        stay='idle'
        if self.move_right==True:
            self.x+=self.speed_x
            stay='run'
            self.flip=False
        if self.move_left==True:
            self.x-=self.speed_x
            self.flip=True
            stay='run'
        if self.xp<25:
            self.speed_x=8
        if self==player:
        
            global zelia_double_jump
            for asd in zelia_double_jump:
                if asd.colliderect(self.new_bbx):
                    zelia_double_jump.remove(asd)
                    global all
                    all['zelia_double_jump']+=1
        self.collisionx()
        self.y+=self.speed_y   
        self.speed_y+=gravition
        self.speed_y = min(self.speed_y, 5)
        self.collisiony()

        if self.speed_y>1 or self.speed_y<-1:
            stay='jump'
        if stay!=self.current:
            self.current=stay
            self.animationsss[self.current].reset()
        if self==player:
            for asd in coins:
                if asd.c_bbx.colliderect(self.new_bbx):
                    self.my_coins+=1
                    coins.remove(asd)
        for asd in projectiles:
            #asd.update()
            p_bbx=asd.get_bbx()

            if p_bbx.colliderect(self.rect()):
                self.xp-=15
                if self!=player:
                    hit_music.play()
                if self==player:
                    self.sparkses=Sparks(asd.x, asd.y, (255, 51, 51))
                    sparksssss.append(self.sparkses)
                if self==player:
                    global scrinshake
                    scrinshake=30
                if self.xp<=0:
                    if self!=player:
                        if self in npss:
                            npss.remove(self)

                    else:
                        
                        exit(0)
                if asd in projectiles:
                    projectiles.remove(asd)
            if mapic.issolid(asd.x, asd.y)==True:
                if asd in projectiles:
                    projectiles.remove(asd)
                self.sparkses=Sparks(asd.x, asd.y, (255, 255, 51))
                sparksssss.append(self.sparkses)
            
        self.animationsss[self.current].update()
        
    def ii(self):
        self.change_gun_timer-=1
        self.change_gun=random.randint(1, 250)
        
        if self.change_gun==3 and self.change_gun_timer<0:
            
            
            if self.now_оружка==self.оружки[0]:
                self.now_оружка=self.оружки[1]
            elif self.now_оружка==self.оружки[1]:
                self.now_оружка=self.оружки[0]

        if self.current=='idle':
            x=random.randint(0, 101)
            if x==1:
                x_go=random.randint(1, 2)
                if x_go==1:
                    self.move_left=True
                else:
                    self.move_right=True
        else:
            x=random.randint(0, 100)
            if x==1:
                self.move_left=False
                self.move_right=False
            self.last_x=self.x
            self.last_y=self.y
            self.update()   
            self.y+=10
            r=self.rect()
            if not mapic.get_intersections(r):
                self.move_left=False
                self.move_right=False
                if self.flip:
                    self.last_x+=5
                else:
                    self.last_x-=5 
            self.x=self.last_x
            self.y=self.last_y
            
        if self.vision_area().colliderect(player.rect()):
            self.fire_timer-=1
            self.move_left=False
            self.move_right=False
            if self.fire_timer==0:
                self.fire()
                self.fire_timer=30

   

        
    def collisiony(self):
        

        self.r=self.rect()
        self.solid_tiles=mapic.get_intersections(self.r)
        for asd in self.solid_tiles:
            if self.speed_y>0:
                self.y=asd.top-self.r.height
                self.jumps=0
                self.speed_y=0
            if self.speed_y<0:
                self.y=asd.bottom
            self.speed_y=0
        if self==player:
            for asd in move_platforms:
                if asd.rect().colliderect(player.new_bbx):
                    if self.y<asd.y:
                        self.y=asd.rect().top-self.r.height
                        self.jumps=0
                        self.speed_y=0
                    else:
                        self.y=asd.rect().bottom
                        
    def collisionx(self):
        self.r=self.rect()
        self.solid_tiles=mapic.get_intersections(self.r)
        for asd in self.solid_tiles:
            if self.move_right==True:
                self.x=asd.left-self.r.width#-self.r.width
                  
            if self.move_left==True:
                self.x=asd.right
    def jump(self):
        if local['zelia_double_jump']==False:
            if self.jumps>0:
                pass
            else:
                self.jumps=1
                self.speed_y=-11
                jump_music.play()
        if local['zelia_double_jump']==True:
            if self.jumps>100 :
                pass
            else:
                self.jumps+=1
                self.speed_y=-11
                jump_music.play()

    def fire(self):
        if self==player:
            if self.pula_timer>0:
                return
        pula_music.play()
        if self.flip==True:
            if self.оружки[0]==self.now_оружка:
                puler=Pula(self.rect().left-50, self.rect().centery, -30, 50)
                if self==player:
                    
                    if local['no_perezaradka']==True:
                        self.timer=0
                    else:
                        self.many_pules+=1
                    if self.many_pules>=3:
                        self.pula_timer=30
                projectiles.append(puler) 
        else:

            if self.оружки[0]==self.now_оружка:
                puler=Pula(self.rect().right+20, self.rect().centery, 30, 50)
                
                if local['no_perezaradka']==True:
                    self.timer=0
                else:                
                    if self==player:
                        self.many_pules+=1
                    if self.many_pules>=3:
                        self.pula_timer=30
                projectiles.append(puler)
        self.y_p=self.rect().top
        if self.flip==True:
            if self.оружки[1]==self.now_оружка:
                if self==player:
                   
                    if local['no_perezaradka']==True:
                        self.timer=0
                    else:
                        self.many_pules+=3
                    if self.many_pules>=3:
                        self.pula_timer=20
                        self.pula_timer-=1
                    for asd in range(3):
                        puler=Pula(self.rect().left-70, self.y_p, -30, 30)
                        self.y_p+=40
                        projectiles.append(puler)
        if self.flip==False:
            if self==player:
                
                if local['no_perezaradka']==True:
                    self.timer=0
                else:
                    self.many_pules+=3
                    if self.many_pules>=3:
                        self.pula_timer=20
                        self.pula_timer-=1
            if self.оружки[1]==self.now_оружка:
                for asd in range(3):
                    puler=Pula(self.rect().right+70, self.y_p, 30, 30)
                    self.y_p+=40
                    projectiles.append(puler)

                    
        


    def vision_area(self):
        if self.flip==False:
            self.vax=self.x+self.rect().width
            self.vay=self.y
            self.va=pygame.Rect(self.vax, self.y, 900, 50)
            return self.va
        if self.flip==True:
            self.vax=self.x-900
            self.vay=self.y
            self.va=pygame.Rect(self.vax, self.y, 900, 50)
            return self.va



class Pula:
    def __init__(self, x, y, speed, max_live_time):
        self.x=x
        self.y=y          
        self.speed=speed
        self.live_time=0
        self.max_live_time=max_live_time
    def update(self):
        self.live_time+=1
        if self.live_time==self.max_live_time:
            projectiles.remove(self)
        self.x+=self.speed
        
        
    def render(self):
        scrin.blit(projectile, (self.x-mapic.camera_x, self.y-mapic.camera_y))
    def get_bbx(self):
        return pygame.Rect(self.x, self.y, projectile.get_width(), projectile.get_height())

class Spark:
    def __init__(self, x, y, color):
        self.speed=random.randint(5, 11)
        self.x=x
        self.y=y
        self.colors=color
        self.r=random.randint(1, 6)
        self.engle=(random.random()-0.5)*4*math.pi
        self.speed_x=self.speed*math.cos(self.engle)
        self.speed_y=self.speed*math.sin(self.engle)
        self.timer=random.randint(20, 76)
    def update(self):
        self.timer-=1
        self.x+=self.speed_x
        self.y+=self.speed_y
    def render(self):
        pygame.draw.circle(scrin, self.colors, (self.x-mapic.camera_x, self.y-mapic.camera_y), self.r)

class Sparks:
    def __init__(self, x, y, color):
        self.sparks=[]
        colors=color
        for asd in range(0, 11):
            self.sp=Spark(x, y, color)        
            self.sparks.append(self.sp)
    def update(self):
        for asd in self.sparks:
            asd.update()
            if asd.timer<0:
                self.sparks.remove(asd)
    def render(self):
        for asd in self.sparks:
            asd.render()
player=Player(mapic.camera_x, mapic.camera_y, False)

zelia_double_jump=[]

def next_lexel(lvl=None):
    global level, mapic, expand, npss, coins, zelia_double_jump
    if lvl is not None:
        level = lvl
    else:
        level += 1
    mapic = map.Tile_map(scrin, level)
    global expand
    expand=1000
    global npss, coins
    npss=[]
    coins=[]
    global move_platforms

    move_platforms=[]
    
    for asd in mapic.get_move_platforms():
        m_p=move_platform.Move_platform(asd[0], asd[1], 5, 5, mapic.resource['popytki_plotform'][0])
        move_platforms.append(m_p)
    global zelia_double_jump
    zelia_double_jump=[]
    for asd in mapic.get_zelia():
        z_d_j=pygame.Rect(asd[0], asd[1], 103.6, 77.6)
        zelia_double_jump.append(z_d_j)
    for asd in mapic.get_coins():
        p=coin.Coin(asd[0], asd[1], (204, 204, 0))
        coins.append(p)
    player.x=mapic.camera_x
    player.y=mapic.camera_y
    for asd in mapic.get_nps():
        p=Player(asd[0], asd[1], True)
        npss.append(p)
main_menu=главное_меню.Main_menu()





coins=[]

for asd in mapic.get_coins():
    p=coin.Coin(asd[0], asd[1], (204, 204, 0))
    coins.append(p)
npss=[]

# mapic.loading()
for asd in mapic.get_nps():
    p=Player(asd[0], asd[1], True)
    npss.append(p)

def start():
    start_time=time.time()
    q=0
    while True:
        
        q+=1
        end_time = time.time()
        if end_time-start_time>=1:
            pygame.display.set_caption(str(q/(end_time-start_time)))
            start_time=time.time()
            q=0
        fps.tick(80)
        scrin.fill((102, 255, 255))
        if player.pula_timer>0:
            player.pula_timer-=1
            if player.pula_timer==0:
                player.many_pules=0 
        

        if player.xp<30:
            player.xp+=0.3
        elif player.xp<100:
            player.xp+=0.1
        else:
            player.xp=100
        
        
        mapic.render()
        mapic.update()
        for asd in coins:
            if abs(player.x-asd.x)+abs(player.y-asd.y)<min_dist:
                asd.render(scrin, mapic)
                asd.update()
        player.update()
        player.render()
        for asd in move_platforms:
            asd.render(scrin, mapic.camera_x, mapic.camera_y)
            asd.update()
        for asd in sparksssss:
            
            asd.update()
            asd.render()
        for enemy in npss:
            if abs(player.x-enemy.x)+abs(player.y-enemy.y)<min_dist:
                enemy.render()
                enemy.ii()
                enemy.update()
        for asd in projectiles:
            asd.update()
        for asd in zelia_double_jump:
            if abs(player.x-asd.x)+abs(player.y-asd.y)<min_dist:
                scrin.blit(mapic.resource['зелья'][0], (asd.x-mapic.camera_x, asd.y-mapic.camera_y))
        global scrinshake
        mapic.camera_x+=(player.x- W//2+250-mapic.camera_x)/30
        mapic.camera_y+=(player.y-H // 2-mapic.camera_y)/30
        mapic.camera_x+=random.randint(-scrinshake, scrinshake)/2
        mapic.camera_y+=random.randint(-scrinshake, scrinshake)/2
        global shrink
        if player.new_bbx.colliderect(mapic.portal_bbx):
            if shrink<=0:
                shrink=1000
       
        if scrinshake>0:
            scrinshake-=1
        for asd in pygame.event.get():
            if asd.type==pygame.QUIT:
                exit(0)
            if asd.type==pygame.KEYDOWN:
                if asd.key==pygame.K_d:
                    player.move_right=True
                    player.move_left=False
                elif asd.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if player.оружки[0]==player.now_оружка:
                    if asd.key==pygame.K_x:
                        player.now_оружка=player.оружки[1]
                elif player.оружки[1]==player.now_оружка:
                    if asd.key==pygame.K_x:
                        player.now_оружка=player.оружки[0]

                if asd.key==pygame.K_a:
                    player.move_right=False
                    player.move_left=True
                if asd.key==pygame.K_SPACE:
                    player.jump()
                if asd.key==pygame.K_f:
                    player.fire()
            if asd.type==pygame.KEYUP:
                if asd.key==pygame.K_d:
                    player.move_right=False
                if asd.key==pygame.K_a:
                    player.move_left=False
        global expand
        if shrink>0:
            scrin_2.fill((0, 0, 0))
            pygame.draw.circle(scrin_2, (0, 0, 0, 0), (W/2, H/2), shrink)
            shrink-=20
            if shrink<=0:
                next_lexel()
            scrin.blit(scrin_2, (0, 0))
        if expand>0:
            scrin_2.fill((0, 0, 0))
            pygame.draw.circle(scrin_2, (0, 0, 0, 0), (W/2, H/2), 1000-expand)
            expand-=20
            scrin.blit(scrin_2, (0, 0))
        pygame.display.update()

main_menu.run(scrin, fps, next_lexel, start, main_menu.run)
