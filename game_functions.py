import sys
import pygame

def check_events():
    """Responds to key and mouse press events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(ai_settings, screen, ship):
    """Updates images on screen and flips to new screen"""
    # Updates screen on each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()