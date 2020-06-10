import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, screen, ai_settings):
        """Initializes the the ship and sets it's initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loads image in and gets it's and screen's rects
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Starts the ship at the bottom center of the screem
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

        # Store a decimal value for the ships center
        self.center = float(self.rect.centerx)
    
    def center_ship(self):
        """Centers the ship"""
        self.center = self.screen_rect.centerx

    def update(self):
        """Updates the position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor 

        # Update rect object from self.center 
        self.rect.centerx = self.center

    def blitme(self):
        """Draws ship at current location"""
        self.screen.blit(self.image, self.rect)