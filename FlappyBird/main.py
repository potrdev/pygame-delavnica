import pygame as pg
import time

pg.init()

def changeY():
    global playerY
    playerY -= 2

#Settings
winX = 800
winY = 500
FPS = 60

#Dislay
display = pg.display.set_mode((winX, winY))

#Pipes
maxPipes = 5

#Player
playerY = 0
isFalling = True

game = True

class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pipes = []

while game:
    #Clock
    pg.time.Clock().tick(FPS)
    display.fill("white")

    #Draw player
    pg.draw.circle(display, "yellow", (50, playerY), 30)

    #Velocity
    if isFalling:
        playerY += 5

    #Get keys
    keys = pg.key.get_pressed()

    #Quit check
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and isFalling:
                isFalling = False
                for i in range(60):
                    changeY()
                isFalling = True

    while len(pipes) <= maxPipes:
        newPipe = Pipe(winX, winY // 2)
        pipes.append(newPipe)

    for pipe in pipes:
        print(len(pipes))
        pipe.x -= 1
        if len(pipes) >= 2:
            pg.draw.circle(display, "green", (pipes[pipes.index(pipe) - 1].x + 30, winY//2), 30)


    
    
                

    pg.display.update()