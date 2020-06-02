import sys
import pygame


def check_keydown_events(event, ship):
    """Checks for keydown presses"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True

def check_keyup_events(event, ship):
    """Checks for keyup presses"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_UP:
            ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False

def check_events(ship):
    """Responds to key and mouse press events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
            
        check_keydown_events(event, ship)
        check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship):
    """Updates images on screen and flips to new screen"""
    # Updates screen on each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()