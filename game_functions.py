import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ship, bullets, ai_settings, screen):
    """Checks for keydown presses"""
    # ship movement keys
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    # bullet fireing key
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)
    
def check_keyup_events(event, ship):
    """Checks for keyup presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship, bullets, ai_settings, screen):
    """Responds to key and mouse press events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, ai_settings, screen)
        elif event.type == pygame.KEYUP:    
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """Delete bullets that go off screen"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(bullets, ai_settings, screen, ship):
    """Fires bullet if there are not too many on screen"""
    if len(bullets) < ai_settings.bullets_allowed:
        # Creates new bullet and adds it to bullet group
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """Updates images on screen and flips to new screen"""
    # Updates screen on each loop
    screen.fill(ai_settings.bg_color)

    # Redraws all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Redraws ship
    ship.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()