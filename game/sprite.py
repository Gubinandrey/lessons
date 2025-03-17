import pygame
pygame.init()
import util
import animation
import map
import random
import math
W =2050
H =1050
scrin=pygame.display.set_mode((W, H), pygame.HWSURFACE | pygame.DOUBLEBUF)
mapic=map.Tile_map(scrin)
fps=pygame.time.Clock()
projectile=util.load('/Users/andrey/python/lessons/game/images/projectile.png', mapic.k-0.2)
gravition=.5
sparksssss=[]
projectiles=[]
scrinshake=0
class Player:
    def __init__(self, x, y, enemy):
        self.x=x
        self.y=y
        self.pula_timer=30
        self.fire_timer=30
        self.xp=100
        self.many_pules=0
        self.gun=util.load('/Users/andrey/python/lessons/game/images/gun.png', mapic.k+1)
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
            scrin.blit(self.gun, (self.rect().right-mapic.camera_x, self.rect().centery-mapic.camera_y))
        else:
            gunimg=pygame.transform.flip(self.gun, True, False)
            gunimg.set_colorkey((0, 0, 0))
            scrin.blit(gunimg, (self.rect().left-12-mapic.camera_x, self.rect().centery-mapic.camera_y))
        for asd in projectiles:
            asd.render()
        pygame.draw.rect(scrin, (255, 0, 0), (self.x-mapic.camera_x, self.y-mapic.camera_y, 60, 10))
        pygame.draw.rect(scrin, (0, 255, 0), (self.x-mapic.camera_x, self.y-mapic.camera_y, 60*self.xp/100, 10))
        
    def update(self):
        stay='idle'
        if self.move_right==True:
            self.x+=self.speed_x
            stay='run'
            self.flip=False
        if self.move_left==True:
            self.x-=self.speed_x
            self.flip=True
            stay='run'
        
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
        for asd in projectiles:
            #asd.update()
            p_bbx=asd.get_bbx()
            
            if p_bbx.colliderect(self.rect()):
                self.xp-=15
                if self==player:
                    global scrinshake
                    scrinshake=30
                if self.xp<=0:
                    if self!=player:
                        npss.remove(self)
                    else:
                        exit(0)
                if asd in projectiles:
                    projectiles.remove(asd)
            if mapic.issolid(asd.x, asd.y)==True:
                if asd in projectiles:
                    projectiles.remove(asd)
                self.sparkses=Sparks(asd.x, asd.y)
                sparksssss.append(self.sparkses)
            
        self.animationsss[self.current].update()
        
    def ii(self):
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

    def rect(self):
        img=self.animationsss[self.current].get_now_img()
        bowdbox=img.get_rect()
        bowdbox.x=self.x
        bowdbox.y=self.y
        self.new_bbx=pygame.Rect(self.x, self.y, bowdbox.width/2, bowdbox.height)
        return self.new_bbx

        
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
        
    def collisionx(self):
        self.r=self.rect()
        self.solid_tiles=mapic.get_intersections(self.r)
        for asd in self.solid_tiles:
            if self.move_right==True:
                self.x=asd.left-self.r.width#-self.r.width
                  
            if self.move_left==True:
                self.x=asd.right
    def jump(self):
        if self.jumps>0:
            pass
        else:
            self.jumps=1
            self.speed_y=-10
    def fire(self):
        if self==player:
            if self.pula_timer>0:
                return
        if self.flip==True:
            puler=Pula(self.rect().left-30, self.rect().centery, -30)
            if self==player:
                self.many_pules+=1
            if self.many_pules>=3:
                self.pula_timer=30
                                
        else:
            puler=Pula(self.rect().right, self.rect().centery, 30)
            if self==player:
                self.many_pules+=1
            if self.many_pules>=3:
                self.pula_timer=30
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
    def __init__(self, x, y, speed):
        self.x=x
        self.y=y          
        self.speed=speed
    def update(self):
        self.x+=self.speed
    def render(self):
        scrin.blit(projectile, (self.x-mapic.camera_x, self.y-mapic.camera_y))
    def get_bbx(self):
        return pygame.Rect(self.x, self.y, projectile.get_width(), projectile.get_height())

class Spark:
    def __init__(self, x, y):
        self.speed=random.randint(5, 11)
        self.x=x
        self.y=y
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
        pygame.draw.circle(scrin, (255, 255, 51), (self.x-mapic.camera_x, self.y-mapic.camera_y), self.r)

class Sparks:
    def __init__(self, x, y):
        self.sparks=[]
        for asd in range(0, 11):
            self.sp=Spark(x, y)        
            self.sparks.append(self.sp)
    def update(self):
        for asd in self.sparks:
            asd.update()
            if asd.timer<0:
                self.sparks.remove(asd)
    def render(self):
        for asd in self.sparks:
            asd.render()









npss=[]

# mapic.loading()
for asd in mapic.get_nps():
    p=Player(asd[0], asd[1], True)
    npss.append(p)
    
player=Player(mapic.camera_x, mapic.camera_y, False)
while True:
    fps.tick(80)
    scrin.fill((102, 255, 255))
    if player.pula_timer>0:
        player.pula_timer-=1
        if player.pula_timer==0:
            player.many_pules=0 
    mapic.render()
    mapic.update()
    player.update()
    player.render()
    for asd in sparksssss:
        asd.update()
        asd.render()
    for enemy in npss:
        enemy.render()
        enemy.ii()
        enemy.update()
    for asd in projectiles:
        asd.update()
    mapic.camera_x+=(player.x-W // 2 -mapic.camera_x)/30
    mapic.camera_y+=(player.y-H // 2-mapic.camera_y)/30
    mapic.camera_x+=random.randint(-scrinshake, scrinshake)/2
    mapic.camera_y+=random.randint(-scrinshake, scrinshake)/2
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
    
    
    pygame.display.update()