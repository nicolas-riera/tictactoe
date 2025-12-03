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
    player2_won = False
    bot_won = False
    winner = ""
    draw = ""
    win_combo = []
    action = None

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
                    if game_mode != None:
                        action = "menu"
                    else:
                        running = False

        screen.fill("white")

        # Main game logic

        # End screen menu action
        if action != None:
            game_mode, player1_won, player2_won, bot_won, winner, draw, action = action_trigger(action)        

        if game_mode is None:
            game_mode, time_count_when_started = main_menu(screen, my_fonts, mouse_clicked)

        elif game_mode == 1:
            if pygame.time.get_ticks() - time_count_when_started >= 500:
                player1_won, bot_won, draw, win_combo = player_solo_play_gui(screen, mouse_clicked, my_fonts)
            else:
                displaygrid_gui(screen)
                
        elif game_mode == 2:
            if pygame.time.get_ticks() - time_count_when_started >= 500:
                player1_won, player2_won, draw, win_combo = player_duo_play_gui(screen, mouse_clicked, my_fonts)
            else:
                displaygrid_gui(screen)

        elif game_mode == 3:
            action = end_screen(screen, winner, my_fonts, mouse_clicked, win_combo)

        game_mode, winner = winner_trigger(player1_won, player2_won, bot_won, draw, game_mode, winner)

        pygame.display.flip()

    pygame.quit()