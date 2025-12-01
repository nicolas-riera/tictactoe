# Librairies
from game import *
from game_gui import *
import pygame

# CLI / Pygame Switch
cli_mode = False

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
else:
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

        screen.fill("blue")

        # Main program

        if "placeholder" == 1:
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