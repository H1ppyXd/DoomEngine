from settings import *
from player import Player
from drawing import Drawing
import pygame_gui


def main_menu():
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    f1 = pygame.font.SysFont('Arial', 72)
    text1 = f1.render('DOOM', True,
                      (255, 255, 255))

    start = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((HALF_WIDTH - 50, HALF_HEIGHT - 75), (100, 50)),
        text='New Game',
        manager=manager
    )

    exit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((HALF_WIDTH - 50, HALF_HEIGHT - 25), (100, 50)),
        text='Exit',
        manager=manager
    )

    run = True
    while run:
        screen.fill(pygame.Color('black'))
        time_delta = clock.tick(75) / 1000.0
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit(-1)
            if events.type == pygame.USEREVENT:
                if events.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if events.ui_element == start:
                        run = False
            manager.process_events(events)
        manager.update(time_delta)
        manager.draw_ui(screen)
        screen.blit(text1, (WIDTH // 2 - 90, 100))
        pygame.display.flip()


pygame.init()
player = Player()
drawing = Drawing(screen)

running = True
main_menu()
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