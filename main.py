import pygame
from constants import *


# Initialize pygame
pygame.init()

# Creates a pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Write a main function that simply prints "Starting asteroids!" (use this exact text).
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw Window
        screen.fill(color="black")
        # Update screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
