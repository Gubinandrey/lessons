import pygame
pygame.init()
import util
import animation
import map


scrin=pygame.display.set_mode((2050, 1050))
fps=pygame.time.Clock()

gravition=0.2
ground=1000
class Player:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.animationsss={
            'idle': animation.Animation('/Users/andrey/python/lessons/game/images/entities/player/idle', 7),
            'run': animation.Animation('/Users/andrey/python/lessons/game/images/entities/player/run', 7),
            'jump': animation.Animation('/Users/andrey/python/lessons/game/images/entities/player/jump', 7)
        }
        self.current='idle'
        self.move_right=False
        self.move_left=False
        self.speed_x=5
        self.speed_y=0
        self.flip=False
        self.timer=120
        self.jumps=0
        #self.sprite=self.animation.get_now_img()
        
       
    def render(self):
        img=pygame.transform.flip(self.animationsss[self.current].get_now_img(), self.flip, False)
        img.set_colorkey((0, 0, 0))
        
        scrin.blit(img, (self.x-mapic.camera_x-self.rect().width/4, self.y-mapic.camera_y))
        
    
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
        self.collisiony()
        if self.speed_y>1 or self.speed_y<-1:
            stay='jump'
        if stay!=self.current:
            self.current=stay
            self.animationsss[self.current].reset()


        self.animationsss[self.current].update()
        
    def ii(self):
        self.timer-=1
        if self.timer==0:
            if self.move_right==True:
                self.move_right=False
                self.move_left=True
                self.timer=120
            else:
                self.move_right=True
                self.move_left=False
                self.timer=120
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
            self.speed_y=-7
    
            
                


npss=[]
enemy=Player(0, 0)
mapic=map.Tile_map(scrin)
mapic.loading()
for asd in mapic.get_nps():
    p=Player(asd[0], asd[1])
    npss.append(p)
player=Player(100+mapic.camera_x, 100+mapic.camera_y)
while True:
    fps.tick(80)
    scrin.fill((102, 255, 255))
    mapic.render()
    mapic.update()
    player.update()
    player.render()
    for enemy in npss:
        enemy.render()
        enemy.ii()
        enemy.update()
    mapic.camera_x+=(player.x-1025-mapic.camera_x)/30
    mapic.camera_y+=(player.y-525-mapic.camera_y)/30



























































    for asd in pygame.event.get():
        if asd.type==pygame.QUIT:
            exit(0)
        if asd.type==pygame.KEYDOWN:
            if asd.key==pygame.K_d:
                player.move_right=True
                player.move_left=False
            if asd.key==pygame.K_a:
                player.move_right=False
                player.move_left=True
            if asd.key==pygame.K_SPACE:
                player.jump()

        if asd.type==pygame.KEYUP:
            if asd.key==pygame.K_d:
                player.move_right=False
            if asd.key==pygame.K_a:
                player.move_left=False
    
    
    pygame.display.update()