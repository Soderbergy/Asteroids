import pygame
from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()  # Always destroy the original

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Too small to split further

        # Split angle
        random_angle = random.uniform(20, 50)

        # Create new velocities
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        # New radius for smaller rocks
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new baby asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2
