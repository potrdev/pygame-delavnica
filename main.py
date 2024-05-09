import pygame

# Init
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Igra")

#Settings

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()