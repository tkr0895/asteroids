import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn_new_asteroids(self):
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        i = 1
        while i >= -1:
            new_velocity = self.velocity.rotate(angle * i)
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velocity * 1.2
            i -= 2

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.spawn_new_asteroids()
        


