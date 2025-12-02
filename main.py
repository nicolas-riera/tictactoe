# cli / pygame Switch
cli_mode = False

# Librairies
from ressources.game import *
from ressources.game_gui import *
import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

    # Variables
    game_mode = None
    mouse_clicked = False
    player1_won = False
    bot_won = False
    winner = ""
    draw = ""

    # pygame setup
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Tic Tac Toe, par Nicolas Riera")
    logo_image = pygame.image.load(os.path.join(BASE_DIR, "ressources", "images", "logo.png"))
    pygame.display.set_icon(logo_image)
    clock = pygame.time.Clock()
    my_fonts = pygame.font.SysFont('Arial', 30), pygame.font.SysFont('Arial', 50)
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
            else:
                mouse_clicked = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    game_mode = None
                    player1_won = False
                    bot_won = False
                    winner = ""
                    draw = ""
                    reset_game()

        screen.fill("white")

        # Main game logic

        if game_mode is None:
            game_mode, time_count_when_started = main_menu(screen, my_fonts, mouse_clicked)

        elif game_mode == 1:
            if pygame.time.get_ticks() - time_count_when_started >= 500:
                player1_won, bot_won, draw = player_solo_play_gui(screen, mouse_clicked, my_fonts)
            else:
                displaygrid_gui(screen)
                
        elif game_mode == 2:
            "placeholder 2 players"

        elif game_mode == 3:
            end_screen(screen, winner)

        if player1_won:
            game_mode = 3
            winner = "player1"
        elif bot_won:
            game_mode = 3
            winner = "bot"
        elif draw:
            game_mode = 3
            winner = "draw"

        pygame.display.flip()

    pygame.quit()