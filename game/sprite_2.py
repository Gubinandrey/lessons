import pygame
pygame.init()
import util
import animation
scrin=pygame.display.set_mode((1535, 810))
fps=pygame.time.Clock()

gravition=0.1
ground=785
class Player:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.animation=animation.Animation('C:/Users/andre/программирование пайтон/game/images/entities/player/run', 6)
        self.move_right=False
        self.move_left=False
        self.speed_x=4
        self.speed_y=0
        self.flip=False
        self.timer=120
        self.sprite=self.animation.get_now_img()
    def render(self):
        img=pygame.transform.flip(self.animation.get_now_img(), self.flip, False)
        scrin.blit(img, (self.x, self.y))
    
    def update(self):
        self.speed_y+=gravition
        self.y+=self.speed_y
        if self.y+self.sprite.get_height()>ground:
            self.y=ground-self.sprite.get_height()
        if self.move_right==True:
            self.x+=3
            self.flip=False
        if self.move_left==True:
            self.x-=3
            self.flip=True
        self.animation.update()
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
player=Player(100, 100)
enemy=Player(0, 0)
while True:
    fps.tick(80)
    scrin.fill((102, 255, 255))
    player.render()
    player.update()
    enemy.render()
    enemy.ii()
    enemy.update()




























































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
        if asd.type==pygame.KEYUP:
            if asd.key==pygame.K_d:
                player.move_right=False
            if asd.key==pygame.K_a:
                player.move_left=False
    pygame.display.update()