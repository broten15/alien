import pygame


class Ship():
    
    def __init__(self, screen, ai_settings):
        """Initializes the the ship and sets it's initial position"""
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
        self.moving_up = False
        self.moving_down = False

        # Store a decimal value for the ships center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        """Updates the position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor     

        # Update rect object from self.center x and y
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery   

    def blitme(self):
        """Draws ship at current location"""
        self.screen.blit(self.image, self.rect)