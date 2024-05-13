import pygame as pg
import random

#Settings
windowX = 700
windowY = 450

FPS = 60

score = 0

font = pg.font.SysFont("Raketa/mont.ttf", 50)

#Player stats
playerPos = [windowX // 2, windowY - 50]
playerSize = 30

playerImage = pg.image.load("Raketa/rocket.png")
player = pg.transform.scale(playerImage, (playerSize + 10, playerSize + 25))

display = pg.display.set_mode((windowX, windowY))
pg.display.set_caption("Raketa")

#Enemy
enemy1Pos = [random.randint(10, windowX - 10), 0]
enemy2Pos = [random.randint(10, windowX - 10), 0]

enemy1Image = pg.image.load("Raketa/enemy_rocket.png")
enemy2Image = pg.image.load("Raketa/enemy_rocket2.png")

enemy1 = pg.transform.scale(enemy1Image, (60,40))
enemy2 = pg.transform.scale(enemy2Image, (60,40))

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

game = True

while game:
    display.fill(BLACK)

    #Text
    text = font.render(f"Score: {score}", True, (255, 255, 255), None)
    display.blit(text, (10,10))

    #Check for quit and press
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerPos[0] -= 10
            if event.key == pg.K_RIGHT:
                playerPos[0] += 10

    #Player
    display.blit(player, (playerPos[0], playerPos[1]))

    #enemies
    if enemy1Pos[1] >= windowY + 20:
        enemy1Pos = [random.randint(10, windowX - 10), 0]
    else:
        enemy1Pos[1] += 0.1

    if enemy2Pos[1] >= windowY + 20:
        enemy2Pos = [random.randint(10, windowX - 10), 0]
    else:
        enemy2Pos[1] += 0.05

    display.blit(enemy1, (enemy1Pos[0], enemy1Pos[1]))
    display.blit(enemy2, (enemy2Pos[0], enemy2Pos[1]))

    #Refresh display
    pg.display.update()