import pygame

# Init
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Igra")

#Settings

#Barve
BLACK = (0,0,0)
WHITE = (255, 255, 255)

exit = False

while not exit:
    # Display
    display.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()