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

# more settings
# player in the middle
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
red = (255, 0, 0)
rect = pygame.Rect(50, 60, 200, 80) # x, y, width, height

# generate background 
def background():
    background = pygame.image.load("bg3.png").convert_alpha() # alpha for png images for transparency
    screen.blit(background, (0, 0)) # attach bg
    pygame.display.flip()
    clock.tick(60) # 60 fps max

def player():
    pygame.draw.rect(screen, red, rect)

# main menu 
def main_menu():
    while running == True:
        for event in pygame.event.get():
            # QUIT event - x clicked on window
            if event.type == pygame.QUIT:
                running = False
                break

# main game
def main_game():
    while running == True:
        for event in pygame.event.get():
            # QUIT event - x clicked on window
            if event.type == pygame.QUIT:
                running = False
                break

# game loop function
def main():
    running = True

    while running == True:
        # check for all occuring events like key presses, mouse moved etc
        for event in pygame.event.get():
            # QUIT event - x clicked on window
            if event.type == pygame.QUIT:
                running = False
                break

        # background()
        screen.fill("blue")
        player()
        pygame.display.flip()


    # if loop ends, quit game
    pygame.quit()

# check if python file is run directly, and not imported etc
if __name__ == "__main__":
    main()


