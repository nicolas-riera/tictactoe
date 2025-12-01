import pygame

def main_menu(screen, my_fonts):
    
    # Surface.render(text, antialias, color, background=None)
    title = my_fonts[1].render("Tic Tac Toe", True, (0, 0, 0))
    screen.blit(title, (293, 200))

    # Draw.rect(surface, color, (x position, y position, x width, y width))
    # pygame.draw.rect(screen, "red", (30, 200, 200, 100))

    pygame.display.flip()