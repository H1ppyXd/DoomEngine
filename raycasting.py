import pygame
from settings import *
from map import *


def foo(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = foo(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for j in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            deep_h = (y - oy) / sin_a
            x = ox + deep_h * cos_a
            if foo(x, y + dy) in world:
                break
            y += dy * TILE
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            deep_v = (x - ox) / cos_a
            y = oy + deep_v * sin_a
            if foo(x + dx, y) in world:
                break
            x += dx * TILE
        #оно и так работает без глобала лол
        deep = deep_v if deep_v < deep_h else deep_h
        deep *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / deep
        c = 255 / (1 + deep ** 2 * 0.00001)
        color = (c, c, c)
        pygame.draw.rect(sc, color, (j * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE