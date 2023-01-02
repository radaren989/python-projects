import random
import pygame as py
import sys

py.init()

size = width,height = 800,600

BG_COLOR = 0,0,0
SNAKE_COLOR = 255,255,255
DOT_COLOR = 255,0,0

screen = py.display.set_mode(size)
class snake():
    def __init__(self, x, y, direction, score):
        self.x = 0
        self.y=0
        self.direction=0
        self.score = 0
        pass
    def move(self):
        #right
        if self.direction == 0:
            self.x+= 20
        #left    
        elif self.direction == 1:
            self.x-=20
        #up
        elif self.direction == 2:
            self.y-=20
        #down    
        elif self.direction == 3:
            self.y+=20    

        if self.x > 800:
            self.x = 0
        elif self.x < 0:
            self.x = 800
        elif self.y > 600:
            self.y = 0
        elif self.y < 0:
            self.y = 610           
        py.draw.rect(screen, SNAKE_COLOR, (self.x,self.y,20,20))



class dot():
    def __init__(self,x,y,amount):
        self.x = 400
        self.y = 300
        self.amount = 1
    
    def draw(self):
        if self.amount == 0:
            self.x = random.randrange(800)
            self.y = random.randrange(600)
            self.amount = 1
        py.draw.rect(screen, DOT_COLOR, (self.x,self.y,10,10))

    def collison(self,snakeX,snakeY):
        if self.x+ 5 > snakeX and self.x+5 <= snakeX + 20 and self.y+5 > snakeY and self.y+5 <= snakeY+20:
            self.amount = 0
            sn.score +=1
            print(sn.score)



clock = py.time.Clock()
sn = snake(0,0,0,0)
col = dot(400,300,1)
while 1:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
        if event.type == py.KEYDOWN:
            keyPressed = event.key
            if keyPressed == py.K_RIGHT:
                sn.direction = 0
            elif keyPressed == py.K_LEFT:
                sn.direction = 1
            elif keyPressed == py.K_UP:
                sn.direction = 2
            elif keyPressed == py.K_DOWN:
                sn.direction = 3   


    screen.fill(BG_COLOR)
    col.draw()
    sn.move()
    col.collison(sn.x,sn.y)
    py.display.update()
    clock.tick(5)