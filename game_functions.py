import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship, bullets, ai_settings, screen):
    """Checks for keydown presses"""
    # Quit game key shortcut
    if  event.key == pygame.K_q:
        sys.exit()

    # ship movement keys
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # bullet fireing key
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)
    
def check_keyup_events(event, ship):
    """Checks for keyup presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, bullets, ai_settings, screen):
    """Responds to key and mouse press events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, ai_settings, screen)
        elif event.type == pygame.KEYUP:    
            check_keyup_events(event, ship)

def update_bullets(bullets, aliens, ai_settings, screen, ship):
    """Update bullet positions and delete bullets that go off screen"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # Checks alien and bullet collisions
    check_alien_bullet_collisions(bullets, aliens, ai_settings, screen, ship)

def check_alien_bullet_collisions(bullets, aliens, ai_settings, screen, ship):
    """Responds to collisions between aliens and bullets"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # Creates new fleet and removes existing bullets
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)

def fire_bullet(bullets, ai_settings, screen, ship):
    """Fires bullet if there are not too many on screen"""
    if len(bullets) < ai_settings.bullets_allowed:
        # Creates new bullet and adds it to bullet group
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)

def get_alien_number_x(ai_settings, alien_width):
    """Gets the amount of aliens that can fit on a row"""
    # find the amount of x space available
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    # find the amout of aliens as an int that can fit in x space available
    alien_number_x = int(available_space_x / (2 * alien_width))   
    return alien_number_x

def get_alien_rows(ai_settings, alien_height, ship_height):
    """Determines the amount of alien rows fit on screen"""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    row_number = int(available_space_y / (2 * alien_height))
    return row_number

def create_alien(ai_settings, screen, alien_number, aliens, row_number):
    """Creates an allien and places it in a row"""
    # gets alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # funtion that gets and sets position of each alien 
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    # adds alien to group  
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    """Creates a fleet of aliens"""
    # create an alien and find the number of rows and aliens in a row
    alien = Alien(ai_settings, screen)
    alien_number_x = get_alien_number_x(ai_settings, alien.rect.width)
    row_number = get_alien_rows(ai_settings, alien.rect.height, ship.rect.height)

    # Create the fleet of aliens
    for row in range(row_number):
        for alien_number in range(alien_number_x):
            create_alien(ai_settings, screen, alien_number, aliens, row)

def check_fleet_edges(aliens, ai_settings):
    """Responds to if fleet has reached the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break

def change_fleet_direction(aliens, ai_settings):
    """Changes fleet direction and drops entire fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(aliens, ai_settings, ship, bullets, stats, screen):
    """Check if fleet is on edge, then update position entire fleet"""
    check_fleet_edges(aliens, ai_settings)
    aliens.update()

    # checks if alien hits ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, aliens, bullets, ai_settings, ship, screen)
    # checks if alien hits bottom of screen
    check_aliens_bottom(stats, aliens, bullets, ai_settings, ship, screen)

def ship_hit(stats, aliens, bullets, ai_settings, ship, screen):
    """Responds apropriately if alien hits ship"""
    if stats.ships_left > 0:
        # Takes away ship life
        stats.ships_left -= 1

        # empty bullet and alien group
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center ship
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # Pause game
        sleep(0.5)
    else:
        # Ends game
        stats.game_active = False

def check_aliens_bottom(stats, aliens, bullets, ai_settings, ship, screen):
    """Checks to see if aliense hove reached the bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # gives same results as if aliens hits hip
            ship_hit(stats, aliens, bullets, ai_settings, ship, screen)
            break

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Updates images on screen and flips to new screen"""
    # Updates screen on each loop
    screen.fill(ai_settings.bg_color)

    # Redraws all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Redraws ship
    ship.blitme()
    # Redraws aliens
    aliens.draw(screen)

    # Make most recently drawn screen visible
    pygame.display.flip()