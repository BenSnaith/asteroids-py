import pygame

from constants import *

def main():
    pygame.init()

    # initalise the display size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0, 0)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=black, rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
