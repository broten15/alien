import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship, bullets, ai_settings, screen, 
        stats, aliens, sb):
    """Checks for keydown presses"""
    # Quit game key shortcut
    if  event.key == pygame.K_q:
        save_high_score(stats)
        sys.exit()

    # ship movement keys
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # bullet fireing key
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)

    # Start game key
    elif event.key == pygame.K_p:
        if not stats.game_active:
            start_game(stats, aliens, bullets, ship, ai_settings, screen, sb)
    
def check_keyup_events(event, ship):
    """Checks for keyup presses"""
    # Movement keys
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, bullets, ai_settings, screen, play_button, 
        stats, aliens, sb):
    """Responds to key and mouse press events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(stats)
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, ai_settings, screen, 
                stats, aliens, sb)
        elif event.type == pygame.KEYUP:    
            check_keyup_events(event, ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_y, mouse_x, play_button, stats, 
                ai_settings, screen, aliens, ship, bullets, sb)

def save_high_score(stats):
    """Saves high score if someone beats it"""
    if stats.score == stats.high_score:
        with open('high_score.txt', 'w') as f_obj:
            f_obj.write(str(stats.score))

def check_play_button(mouse_y, mouse_x, play_button, stats, ai_settings, 
        screen, aliens, ship, bullets, sb):
    """Starts a new game if the player clicks play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats, aliens, bullets, ship, ai_settings, screen, sb)

def start_game(stats, aliens, bullets, ship, ai_settings, screen, sb):
    """Initializes and starts game"""
    # Resets dynamic settings
    ai_settings.initialize_dynamic_settings()

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)
    
    # Reset the game statistics
    stats.reset_stats()
    stats.game_active = True

    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()

    # Empty the group of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()    

def update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb):
    """Update bullet positions and delete bullets that go off screen"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # Checks alien and bullet collisions
    check_alien_bullet_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb)

def check_alien_bullet_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb):
    """Responds to collisions between aliens and bullets"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    # Adds points in bullet hits aliens
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Starts new level if fleet is destroyed
        bullets.empty()
        ai_settings.speedup_game()

        # Increase level number
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, aliens, ship)

def check_high_score(stats, sb):
    """If score is greater than high score, high score updates with current one"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

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
    row_number = get_alien_rows(ai_settings, alien.rect.height, 
                    ship.rect.height)

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

def update_aliens(aliens, ai_settings, ship, bullets, stats, screen, sb):
    """Check if fleet is on edge, then update position entire fleet"""
    check_fleet_edges(aliens, ai_settings)
    aliens.update()

    # checks if alien hits ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, aliens, bullets, ai_settings, ship, screen, sb)
    # checks if alien hits bottom of screen
    check_aliens_bottom(stats, aliens, bullets, ai_settings, ship, screen, sb)

def ship_hit(stats, aliens, bullets, ai_settings, ship, screen, sb):
    """Responds apropriately if alien hits ship"""
    if stats.ships_left > 0:
        # Takes away ship life
        stats.ships_left -= 1

        # Redraws ships lives
        sb.prep_ships()

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
        pygame.mouse.set_visible(True)

def check_aliens_bottom(stats, aliens, bullets, ai_settings, ship, screen, sb):
    """Checks to see if aliense hove reached the bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # gives same results as if aliens hits hip
            ship_hit(stats, aliens, bullets, ai_settings, ship, screen, sb)
            break

def update_screen(ai_settings, screen, ship, bullets, aliens, 
        stats, play_button, sb):
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

    # Draw the score information
    sb.show_score()

    # Draw play button if game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make most recently drawn screen visible
    pygame.display.flip()