from ressources.game import *
import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main_menu(screen, my_fonts, mouse_clicked):

    logo_title = pygame.image.load(os.path.join(BASE_DIR, "images", "logo_title.png"))
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
                return 1
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)        
        elif 560 <= pygame.mouse.get_pos()[1] <= 639:
            if mouse_clicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return 2
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()

    return None

def displaygrid_gui(screen, mouse_clicked):

    index_display_positions = [
        (50, 53), (290, 53), (520, 53),
        (50, 288), (290, 288), (520, 288),
        (50, 518), (290, 518), (520, 518)
    ]

    screen.fill("white")

    X_symbol = pygame.image.load(os.path.join(BASE_DIR, "images", "X.png"))
    X_symbol_scaled = pygame.transform.scale(X_symbol, (X_symbol.get_size()[0]*0.7, X_symbol.get_size()[1]*0.7))
    O_symbol = pygame.image.load(os.path.join(BASE_DIR, "images", "O.png"))
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

    pygame.display.flip()

def placesymbol_player_gui(value, mouse_clicked):

    # Symbol assignation
    if value == "player1":
        symbol = "X"
    elif value == "player2":
        symbol = "O" 

    # Hitboxes coordonnees
    index_display_hitboxes = [
        ((50, 53), (278, 274)), ((289, 53), (508, 274)), ((520, 53), (747, 274)), 
        ((50, 288), (280, 508)), ((289, 288), (510, 508)), ((520, 288), (747, 508)),
        ((50, 518), (280, 748)), ((290, 518), (510, 748)), ((520, 518), (747, 748))
    ]

    match pygame.mouse.get_pos():
        case (x, y) if index_display_hitboxes[0][0][0] <= x <= index_display_hitboxes[0][1][0] and index_display_hitboxes[0][0][1] <= y <= index_display_hitboxes[0][1][1]:
            if mouse_clicked and grid[0] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[0] = symbol
            elif grid[0] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[1][0][0] <= x <= index_display_hitboxes[1][1][0] and index_display_hitboxes[1][0][1] <= y <= index_display_hitboxes[1][1][1]:
            if mouse_clicked and grid[1] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[1] = symbol
            elif grid[1] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[2][0][0] <= x <= index_display_hitboxes[2][1][0] and index_display_hitboxes[2][0][1] <= y <= index_display_hitboxes[2][1][1]:
            if mouse_clicked and grid[2] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[2] = symbol
            elif grid[2] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[3][0][0] <= x <= index_display_hitboxes[3][1][0] and index_display_hitboxes[3][0][1] <= y <= index_display_hitboxes[3][1][1]:
            if mouse_clicked and grid[3] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[3] = symbol
            elif grid[3] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[4][0][0] <= x <= index_display_hitboxes[4][1][0] and index_display_hitboxes[4][0][1] <= y <= index_display_hitboxes[4][1][1]:
            if mouse_clicked and grid[4] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[4] = symbol
            elif grid[4] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[5][0][0] <= x <= index_display_hitboxes[5][1][0] and index_display_hitboxes[5][0][1] <= y <= index_display_hitboxes[5][1][1]:
            if mouse_clicked and grid[5] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[5] = symbol
            elif grid[5] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[6][0][0] <= x <= index_display_hitboxes[6][1][0] and index_display_hitboxes[6][0][1] <= y <= index_display_hitboxes[6][1][1]:
            if mouse_clicked and grid[6] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[6] = symbol
            elif grid[6] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[7][0][0] <= x <= index_display_hitboxes[7][1][0] and index_display_hitboxes[7][0][1] <= y <= index_display_hitboxes[7][1][1]:
            if mouse_clicked and grid[7] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[7] = symbol
            elif grid[7] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case (x, y) if index_display_hitboxes[8][0][0] <= x <= index_display_hitboxes[8][1][0] and index_display_hitboxes[8][0][1] <= y <= index_display_hitboxes[8][1][1]:
            if mouse_clicked and grid[8] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                grid[8] = symbol
            elif grid[8] == 0:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        case _:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    

def player_solo_play_gui(screen, mouse_clicked):

    displaygrid_gui(screen, mouse_clicked)

    placesymbol_player_gui("player1", mouse_clicked)
    