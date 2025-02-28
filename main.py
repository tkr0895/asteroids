import pygame
from constants import *

def startup_print():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def set_variables_for_game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    return screen, clock, dt

def game_loop(screen, clock, dt):
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main():
    pygame.init()
    startup_print()
    screen, clock, dt = set_variables_for_game_loop()
    game_loop(screen, clock, dt)

if __name__ == "__main__":
    main()