import pygame as pg
import random
import time

pg.init()
pg.font.init()

#Settings
windowX = 700
windowY = 450

FPS = 60

score = 0

font = pg.font.SysFont("mont.ttf", 50)

#Player stats
playerPos = [windowX // 2, windowY - 50]
playerSize = 30

playerImage = pg.image.load("rocket.png")
player = pg.transform.scale(playerImage, (playerSize + 10, playerSize + 25))

display = pg.display.set_mode((windowX, windowY))
pg.display.set_caption("Raketa")

#Enemy
enemy1Pos = [random.randint(10, windowX - 10), 0]
enemy2Pos = [random.randint(10, windowX - 10), 0]

enemy1Image = pg.image.load("enemy_rocket.png")
enemy2Image = pg.image.load("enemy_rocket2.png")

enemy1 = pg.transform.scale(enemy1Image, (60,40))
enemy2 = pg.transform.scale(enemy2Image, (60,40))

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#Bullet
bulletPos = [0,0]

game = True
bulletOnScreen = False

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

bullets = []

while game:
    display.fill(BLACK)

    #Text
    text = font.render(f"Score: {score}", True, (255, 255, 255), None)
    display.blit(text, (10,10))

    #Check for quit and press
    mouse = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                newBullet = Bullet(playerPos[0], playerPos[1])
                bullets.append(newBullet)

    for bullet in bullets:
        bullet.y -= 0.5
        pg.draw.circle(display, WHITE, (bullet.x, bullet.y), 10)
        if enemy1Pos[0] >=bullet.x - 50 and enemy1Pos[0] <= bullet.x + 50 and enemy1Pos[1] >= bullet.y - 50 and enemy1Pos[1] <= bullet.y + 50:
            bullets.pop(bullets.index(bullet))
            enemy1Pos = [random.randint(10, windowX - 30), 0]
            score += 1
        if enemy2Pos[0] >=bullet.x - 50 and enemy2Pos[0] <= bullet.x + 50 and enemy2Pos[1] >= bullet.y - 50 and enemy2Pos[1] <= bullet.y + 50:
            bullets.pop(bullets.index(bullet))
            enemy2Pos = [random.randint(10, windowX - 30), 0]
            score += 1

    playerPos = [mouse[0], windowY - 60]

    #Check for collision
    if enemy1Pos[0] >= playerPos[0] - 20 and enemy1Pos[0] <= playerPos[0] + 20 and enemy1Pos[1] >= playerPos[1] - 20 and enemy1Pos[1] <= playerPos[1] + 20 or enemy1Pos[1] >= windowY:
        diedText = font.render(f"You died!", True, (255, 255, 255), None)
        display.blit(diedText, (windowX // 2 - 80, windowY // 2 - 30))
        pg.display.update()
        time.sleep(2)
        game = False
    
    if enemy2Pos[0] >= playerPos[0] - 20 and enemy2Pos[0] <= playerPos[0] + 20 and enemy2Pos[1] >= playerPos[1] - 20 and enemy2Pos[1] <= playerPos[1] + 20 or enemy2Pos[1] >= windowY:
        diedText = font.render(f"You died!", True, (255, 255, 255), None)
        display.blit(diedText, (windowX // 2 - 80, windowY // 2 - 30))
        pg.display.update()
        time.sleep(2)
        game = False

    #Player
    display.blit(player, (playerPos[0], playerPos[1]))

    #enemies
    if enemy1Pos[1] >= windowY + 20:
        enemy1Pos = [random.randint(10, windowX - 30), 0]
        score += 1
    else:
        enemy1Pos[1] += 0.1

    if enemy2Pos[1] >= windowY + 20:
        enemy2Pos = [random.randint(10, windowX - 30), 0]
        score += 1
    else:
        enemy2Pos[1] += 0.06
        

    display.blit(enemy1, (enemy1Pos[0], enemy1Pos[1]))
    display.blit(enemy2, (enemy2Pos[0], enemy2Pos[1]))

    #Refresh display
    pg.display.update()