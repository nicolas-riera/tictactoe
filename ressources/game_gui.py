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
                return 1
            elif 560 <= pygame.mouse.get_pos()[1] <= 639:
                return 2

    pygame.display.flip()

    return None