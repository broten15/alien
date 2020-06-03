import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
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

    # Main loop for game
    while True:
        gf.check_events(ship, bullets, ai_settings, screen)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()