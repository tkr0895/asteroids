import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

black = (0, 0, 0)
score = 0

def startup_print():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def set_variables_for_game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    return screen, clock, dt

def player_hit_asteroid(asteroids, other):
    for asteroid in asteroids:
            collision = asteroid.check_collision(other)
            if collision:
                return True

def bullet_hit_asteroid(asteroids, others):
    for asteroid in asteroids:
        for other in others:
            collision = asteroid.check_collision(other)
            if collision:
                handle_asteroid_hit(asteroid, other)

def add_score():
    global score
    score = score + 10 

def handle_asteroid_hit(asteroid, other):
    asteroid.split()
    other.kill()
    add_score()

def game_loop(screen, clock, dt, updateables, drawables, asteroids, player, shots):
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill(BLACK)
        updateables.update(dt)
        if player_hit_asteroid(asteroids, player):
            end_print()
            exit()
        bullet_hit_asteroid(asteroids, shots)
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

def add_containers(updatables, drawables, asteroids, shots):
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables, shots)

def end_print():
    global score
    print(f"Game over!")
    print(f"You reached {score} points")

def init_game():
    pygame.init()
    startup_print()
    screen, clock, dt = set_variables_for_game_loop()
    updatables, drawables, asteroids, shots = add_groups()
    add_containers(updatables, drawables, asteroids, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    return screen, clock, dt, updatables, drawables, asteroids, shots, player,

def main():
    screen, clock, dt, updatables, drawables, asteroids, shots, player = init_game()
    game_loop(screen, clock, dt, updatables, drawables, asteroids, player, shots)

if __name__ == "__main__":
    main()