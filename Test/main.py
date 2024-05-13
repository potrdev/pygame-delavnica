import pygame

from random import randint

import time

pygame.init()
pygame.font.init()

#Settings
pygame.display.set_caption("Igra")
FPS = 60

window_X = 650
window_Y = 400
X = window_X - 40
Y = window_Y - 40

display = pygame.display.set_mode((window_X,window_Y))

font = pygame.font.SysFont("mont.ttf", 50)

# Props
score = 0
level2 = False
level3 = False

#Circle
circle_x = randint(1, X)
circle_y = randint(1 ,Y)

circlemove = [circle_x,circle_y]

#Barve
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
PINK = (255, 50, 150)

exit = False
lost = False
win = False

while not exit:
    # Display
    display.fill(WHITE)
    
    # Check score
    if score <= -5:
        lost = True
        loseText = font.render(f"YOU LOST!", True, BLACK, None)
        display.blit(loseText, (window_X // 3, window_Y // 3))


    if score >= 25:
        win = True
        winText = font.render(f"YOU WIN!", True, BLACK, None)
        display.blit(winText, (window_X // 3, window_Y // 3))


    #BG
    if not win and not lost:
        bg = pygame.image.load("bg.jpg").convert_alpha()
        display.blit(bg, (0,0))

    # Mouse
    mousepos = pygame.mouse.get_pos()

    #Elements
    if not level2 and not level3:
        circle = pygame.draw.circle(display, WHITE, (circlemove[0], circlemove[1]), 25)
    elif not level2 and level3:
        circle = pygame.draw.circle(display, PINK, (circlemove[0], circlemove[1]), 25)
    
    if score == 5:
        level2 = True

    if score == 10:
        level3 = True

    if level2:
        circlemove[0] += 10
    else:
        circlemove[0] += 5

    if circle[0] >= window_X:
        circlemove[0] = randint(1,X // 3)
        circlemove[1] = randint(1,Y // 3)
        display.blit(text, (10,10))
        score -= 1


    #Text
    text = font.render(f"Score: {score}", True, (255, 255, 255), None)
    display.blit(text, (10,10))

    if not level2:
        levelText = font.render(f"Level: 1", True, (255, 255, 255), None)
        display.blit(levelText, (10,50))
    else:
        levelText = font.render(f"Level: 2", True, (255, 255, 255), None)
        display.blit(levelText, (10,50))

    #Input
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = circle.collidepoint(pygame.mouse.get_pos())
            if click == 1:
                score += 1
            else:
                score -= 1
            circlemove[0] = randint(1,X // 2)
            circlemove[1] = randint(1,Y // 2)
            display.blit(text, (10,10))
                            

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
