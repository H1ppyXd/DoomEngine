import pygame
from settings import *
from raycasting import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont(None, 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, sky, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, ground, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, red)
        self.sc.blit(render, (10, 10))