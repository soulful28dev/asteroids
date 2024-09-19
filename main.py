import pygame
from constants import *

def main():
    pygame.init()
    screen_bg_color = (0, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        pygame.Surface.fill(screen, screen_bg_color, rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()


#  ➜ asteroids (main) ✗ source venv/bin/activate