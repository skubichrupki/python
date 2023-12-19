import pygame
import time
import random

# window settings
pygame.init()
clock = pygame.time.Clock()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Light Souls")

def background():
    background = pygame.image.load("bg3.png").convert_alpha()
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# main game loop function
def main():
    running = True

    while running == True:
        # check for all occuring events like key presses, mouse moved etc
        for event in pygame.event.get():

            # QUIT event - x clicked on window
            if event.type == pygame.QUIT:
                running = False
                break

        background()
        


    # if loop ends, quit game
    pygame.QUIT

# check if python file is run directly, and not imported etc
if __name__ == "__main__":
    main()


