from settings import *

text_map = [
    '111111111111',
    '1......1...1',
    '1..11111.111',
    '1....1.....1',
    '1..1....1..1',
    '1..1.1..1111',
    '1....1.....1',
    '111111111111'
]

world = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world.add((i * TILE, j * TILE))