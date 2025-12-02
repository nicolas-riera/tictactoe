# Librairies
from ressources.game import *
import time
import pygame
import os

# Variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player1_has_played = False
bot_has_played = True

# Image loading
X_symbol = pygame.image.load(os.path.join(BASE_DIR, "images", "X.png"))
O_symbol = pygame.image.load(os.path.join(BASE_DIR, "images", "O.png"))
logo_title = pygame.image.load(os.path.join(BASE_DIR, "images", "logo_title.png"))

def reset_game():
    global grid
    global player1_has_played
    global bot_has_played

    grid = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
    player1_has_played = False
    bot_has_played = True

def main_menu(screen, my_fonts, mouse_clicked):

    logo_title_rect = logo_title.get_rect(center=(650, 500))
    logo_title_scaled = pygame.transform.scale(logo_title, (logo_title.get_size()[0]*0.5, logo_title.get_size()[1]*0.5))
    screen.blit(logo_title_scaled, logo_title_rect)

    # Draw.rect(surface, color, (x position, y position, x width, y width))
    pygame.draw.rect(screen, (255, 107, 107), (295, 450, 203, 80))
    player1_button = my_fonts[0].render("1 Joueur", True, (0, 0, 0))
    screen.blit(player1_button, (350, 470))
    pygame.draw.rect(screen, (107, 137, 255), (295, 560, 203, 80))
    player2_button = my_fonts[0].render("2 Joueurs", True, (0, 0, 0))
    screen.blit(player2_button, (345, 580))

    if 295 <= pygame.mouse.get_pos()[0] <= 497:
        if 449 <= pygame.mouse.get_pos()[1] <= 529:
            if mouse_clicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return 1, pygame.time.get_ticks()
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)        
        elif 560 <= pygame.mouse.get_pos()[1] <= 639:
            if mouse_clicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return 2, pygame.time.get_ticks()
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()

    return None, 0

def displaygrid_gui(screen):

    index_display_positions = [
        (50, 53), (290, 53), (520, 53),
        (50, 288), (290, 288), (520, 288),
        (50, 518), (290, 518), (520, 518)
    ]

    X_symbol_scaled = pygame.transform.scale(X_symbol, (X_symbol.get_size()[0]*0.7, X_symbol.get_size()[1]*0.7))
    O_symbol_scaled = pygame.transform.scale(O_symbol, (O_symbol.get_size()[0]*0.7, O_symbol.get_size()[1]*0.7))

    pygame.draw.rect(screen, (0, 0, 0), (280, 50, 10, 700))
    pygame.draw.rect(screen, (0, 0, 0), (510, 50, 10, 700))
    pygame.draw.rect(screen, (0, 0, 0), (50, 280, 700, 10))
    pygame.draw.rect(screen, (0, 0, 0), (50, 510, 700, 10))

    for i in range(len(grid)):
        if grid[i] == "X":
            X_symbol_rect = X_symbol.get_rect(topleft=index_display_positions[i])    
            screen.blit(X_symbol_scaled, X_symbol_rect) 
        elif grid[i] == "O":
            O_symbol_rect = O_symbol.get_rect(topleft=index_display_positions[i])    
            screen.blit(O_symbol_scaled, O_symbol_rect)

def placesymbol_player_gui(value, screen, mouse_clicked, my_fonts):

    global player1_has_played
    global bot_has_played

    # Symbol assignation
    if value == "player1":
        symbol = "X"
        player1_turn = my_fonts[0].render("Joueur 1, à ton tour !", True, (0, 0, 0))
        screen.blit(player1_turn, (282, 755))
    elif value == "player2":
        symbol = "O"
        player1_turn = my_fonts[0].render("Joueur 2, à ton tour !", True, (0, 0, 0))
        screen.blit(player1_turn, (282, 755)) 

    # Hitboxes coordonnees
    index_display_hitboxes = [
        ((50, 53), (278, 274)), ((289, 53), (508, 274)), ((520, 53), (747, 274)), 
        ((50, 288), (280, 508)), ((289, 288), (510, 508)), ((520, 288), (747, 508)),
        ((50, 518), (280, 748)), ((290, 518), (510, 748)), ((520, 518), (747, 748))
    ]

    cursor_set = False
    for i in range(len(grid)):

        x, y = pygame.mouse.get_pos()
        
        if index_display_hitboxes[i][0][0] <= x <= index_display_hitboxes[i][1][0] and index_display_hitboxes[i][0][1] <= y <= index_display_hitboxes[i][1][1]:
            if mouse_clicked and grid[i] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[i] = symbol
                player1_has_played = True
                bot_has_played = False
            elif grid[i] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            cursor_set = True
            break

    if not cursor_set:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()  
    
    return checkvictory(grid, "X", None, False)

def placesymbol_bot_gui(screen, my_fonts):

    global player1_has_played
    global bot_has_played

    screen.fill("white")
    displaygrid_gui(screen)

    player1_turn = my_fonts[0].render("L'ordinateur réfléchit...", True, (0, 0, 0))
    screen.blit(player1_turn, (282, 755))

    pygame.display.flip() 

    time.sleep(2)

    grid[ordinateur(grid, "O", False)] = "O"
    player1_has_played = False
    bot_has_played = True

    return checkvictory(grid, "O", None, False)

def player_solo_play_gui(screen, mouse_clicked, my_fonts):

    player1_won = False
    bot_won = False
    draw = False

    displaygrid_gui(screen)

    if not(player1_has_played):
        player1_won = placesymbol_player_gui("player1", screen, mouse_clicked, my_fonts)

    displaygrid_gui(screen)

    if 0 in grid and not(player1_won):
        if not(bot_has_played):
            bot_won = placesymbol_bot_gui(screen, my_fonts)

    elif (not 0 in grid):
        return False, False, True

    return player1_won, bot_won, draw

def end_screen(screen, winner):
    
    displaygrid_gui(screen)
    screen.set_alpha(160)
    pygame.display.flip()
