import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

black = (0, 0, 0)

def startup_print():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def set_variables_for_game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    return screen, clock, dt

def check_for_collisions(asteroids, player):
    for asteroid in asteroids:
            collision = asteroid.check_collision(player)
            if collision:
                print("Game over!")
                exit()

def game_loop(screen, clock, dt, updateables, drawables, asteroids, player):
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill(BLACK)
        updateables.update(dt)
        check_for_collisions(asteroids, player)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def add_groups():
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    return updatables, drawables, asteroids, shots

def add_containers(updatables, drawables, asteroids):
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables)

def main():
    pygame.init()
    startup_print()
    screen, clock, dt = set_variables_for_game_loop()
    updatables, drawables, asteroids, shots = add_groups()
    add_containers(updatables, drawables, asteroids)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    game_loop(screen, clock, dt, updatables, drawables, asteroids, player)

if __name__ == "__main__":
    main()