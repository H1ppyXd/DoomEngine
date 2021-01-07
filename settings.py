import math
import pygame


WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Doom')
clock = pygame.time.Clock()
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TILE = 100
red = pygame.Color(220, 0, 0)
ground = pygame.Color(40, 40, 40)
sky = pygame.Color(0, 156, 235)
MAP_SCALE = 5
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)
MAP_TILE = TILE // MAP_SCALE
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 900
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * TILE
SCALE = WIDTH // NUM_RAYS
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 0.5


