from settings import *
from player import Player
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Doom')
player = Player()
drawing = Drawing(screen)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.movement()


    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick()