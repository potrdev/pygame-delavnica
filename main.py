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
clicked = False
start = time.time()
delay = 5

#Circle
circle_x = randint(1, X)
circle_y = randint(1 ,Y)

#Barve
BLACK = (0,0,0)
WHITE = (255, 255, 255)

exit = False

while not exit:
    # Check score
    if score <= -5:
        break

    # Display
    display.fill(WHITE)

    #BG
    bg = pygame.image.load("bg.jpg").convert_alpha()
    display.blit(bg, (0,0))

    # Mouse
    mousepos = pygame.mouse.get_pos()

    #Elements
    circle = pygame.draw.circle(display, WHITE, (circle_x, circle_y), 25)

    #Text
    text = font.render(f"Score: {score}", True, (255, 255, 255), None)
    display.blit(text, (10,10))

    #Input
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = circle.collidepoint(pygame.mouse.get_pos())
            if click == 1:
                clicked = True
                circle_x = randint(1,X)
                circle_y = randint(1,Y)
                score += 1
                display.blit(text, (10,10))
                clicked = False

    if time.time() - start >= delay:
        if clicked == False:
            circle_x = randint(1,X)
            circle_y = randint(1,Y)
            score -= 1
            display.blit(text, (10,10))                      

            pygame.display.update()
            pygame.time.Clock().tick(FPS)
