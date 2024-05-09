import pygame

from random import randint

#Settings
pygame.display.set_caption("Igra")
FPS = 60
X = 650
Y = 400


display = pygame.display.set_mode((X,Y))

#Circle
circle_x = randint(1, X)
circle_y = randint(1 ,Y)

#Barve
BLACK = (0,0,0)
WHITE = (255, 255, 255)

exit = False

while not exit:
    # Display
    display.fill(WHITE)

    #BG
    bg = pygame.image.load("bg.jpg")
    display.blit(bg, (0,0))

    #Elements
    pygame.draw.circle(display, WHITE, (circle_x, circle_y), 25)

    #Input
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if keys[pygame.K_SPACE]:
            circle_x = randint(1,X)
            circle_y = randint(1,Y)
            

    pygame.display.update()
    pygame.time.Clock().tick(FPS)