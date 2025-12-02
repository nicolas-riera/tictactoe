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

    if mouse_clicked :
        if 295 <= pygame.mouse.get_pos()[0] <= 497:
            if 449 <= pygame.mouse.get_pos()[1] <= 529:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return 1
            elif 560 <= pygame.mouse.get_pos()[1] <= 639:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return 2
            
    if 295 <= pygame.mouse.get_pos()[0] <= 497:
            if 449 <= pygame.mouse.get_pos()[1] <= 529:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif 560 <= pygame.mouse.get_pos()[1] <= 639:
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

def player_solo_play_gui(screen, mouse_clicked):

    displaygrid_gui(screen, mouse_clicked)

    