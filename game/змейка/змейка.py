import pygame
import random
pygame.init()
font=pygame.font.SysFont('Futura', (100))
font1=pygame.font.SysFont('Futura', (95))
font2=pygame.font.SysFont('Futura', (40))
speed_head=3
scrin=pygame.display.set_mode((600, 600))
fps=pygame.time.Clock()
snake_size=15
trap=None
eat=[random.randint(0, 600//snake_size-1), random.randint(0, 600//snake_size-1)]
music1=pygame.mixer.Sound('game/defeat.mp3')
eat_count=0
head=[30, 30]
snake=[head, ]
rect_movie_up=False
rect_movie_down=False
rect_movie_left=False
rect_movie_right=True
game_ower=False
while True:
    fps.tick(10)
    scrin.fill((204, 255, 153))
    if game_ower==False:
        pygame.draw.rect(scrin, (0, 255, 255), (snake[0][0]*snake_size, snake[0][1]*snake_size, snake_size, snake_size))
        for asd in snake[1:]:    
            pygame.draw.rect(scrin, (0, 0, 204,), (asd[0]*snake_size, asd[1]*snake_size, snake_size, snake_size))
        pygame.draw.rect(scrin, (255, 0, 0), (eat[0]*snake_size,  eat[1]*snake_size, snake_size, snake_size))
        for awsd in range(len(snake)-1, 0, -1):
            snake[awsd]=snake[awsd-1].copy()
            
        if rect_movie_right==True:
            head[0]+=1
        if rect_movie_left==True:
            head[0]-=1
        if rect_movie_down==True:
            head[1]+=1
        if rect_movie_up==True:
            head[1]-=1
        if head[0]>=600//snake_size:
            head[0]=0
        if head[0]<0:
            head[0]=600//snake_size-1
        if head[1]>=600//snake_size:
            head[1]=0
        if head[1]<0:
            head[1]=600//snake_size-1
        if head==eat:
            eat=[random.randint(0, 600//snake_size-1), random.randint(0, 600//snake_size-1)]
            tail=[-1, -1]
            snake.append(tail)
            eat_count+=1

        if eat_count==6:
            trap=[random.randint(0, 600//snake_size-1), random.randint(0, 600//snake_size-1)]
            eat_count=0
        if trap!=None:
            pygame.draw.rect(scrin, (0, 0, 0), (trap[0]*snake_size, trap[1]*snake_size, snake_size, snake_size))
        if head==trap:
            snake=snake[ :-1]
            trap=None
        for awsd in range(len(snake)-1, 0, -1):
            if snake[awsd]==head:
                game_ower=True
                music1.play()
        for asd in pygame.event.get():
            if asd.type==pygame.QUIT:
                exit(0)
            if asd.type==pygame.KEYDOWN:
                if asd.key==pygame.K_UP:
                    if rect_movie_down!=True:
                        rect_movie_up=True
                        rect_movie_down=False
                        rect_movie_left=False
                        rect_movie_right=False
                if asd.key==pygame.K_DOWN:
                    if rect_movie_up!=True:
                        rect_movie_up=False
                        rect_movie_down=True
                        rect_movie_left=False
                        rect_movie_right=False
                if asd.key==pygame.K_LEFT:
                    if rect_movie_right!=True:
                        rect_movie_up=False
                        rect_movie_down=False
                        rect_movie_left=True
                        rect_movie_right=False
                if asd.key==pygame.K_RIGHT:
                    if rect_movie_left!=True:
                        rect_movie_up=False
                        rect_movie_down=False
                        rect_movie_left=False
                        rect_movie_right=True
        
    if game_ower==True:
        bot_text1=font.render(str('GAME'), True, (255, 0, 0))
        bot_text2=font1.render(str('OVER'), True, (255, 0, 0))
        bot_text3=font2.render(str('чтобы начать игру заново нажмите пробел'), True, (102, 0, 204))
        bot_text4=font2.render(str('enter space to restart'), True, (102, 0, 204))
        scrin.blit(bot_text1, (190, 60))
        scrin.blit(bot_text2, (205, 150))
        scrin.blit(bot_text3, (10, 300))
        scrin.blit(bot_text4, (150, 350))
        for asd in pygame.event.get():
            if asd.type==pygame.QUIT:
                exit(0)
            if asd.type==pygame.KEYDOWN:
                if asd.key==pygame.K_SPACE:
                    head=[30, 30]
                    snake=[head]
                    eat=[random.randint(0, 600//snake_size-1), random.randint(0, 600//snake_size-1)]
                    game_ower=False
                    music1.stop()
                    trap=None
                    eat_count=0
    pygame.display.update()