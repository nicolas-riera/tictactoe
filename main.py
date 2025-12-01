# cli / pygame Switch
cli_mode = False

# Librairies
from game import *
from game_gui import *
import pygame

# cli mode
if cli_mode:
    if player_selection() == 1:
        # Loop for single-player mode
        while True:
            if player_solo_play():
                continue
            else:
                break

    else:
        # Loop for two-player mode
        while True:
            if player_duo_play():
                continue
            else:
                break

# Pygame mode
else:

    game_mode = None

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        # Main program

        if game_mode is None:
            main_menu(screen)

        elif game_mode == 1:
            # Loop for single-player mode
            while True:
                if "placeholder":
                    continue
                else:
                    break
        else:
            # Loop for two-player mode
            while True:
                if "placeholder":
                    continue
                else:
                    break

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()