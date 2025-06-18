import pygame
from circleshape import CircleShape
from constants import SHOT_RAIDIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RAIDIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RAIDIUS)

    def update(self, dt):
        self.position += self.velocity * dt
