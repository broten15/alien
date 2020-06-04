import sys
import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Initialize game and make a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen, ai_settings)
    # Make a group to store bullets
    bullets = Group()
    # Make a group to store aliens
    aliens = Group()

    # Create an instance to store game stats
    stats = GameStats(ai_settings)

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # Main loop for game
    while True:
        gf.check_events(ship, bullets, ai_settings, screen)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            gf.update_aliens(aliens, ai_settings, ship, bullets, stats, screen)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
