import pygame

class Ship():
    
    def __init__(self, screen):
        """Initializes the the ship and sets it's initial position"""
        self.screen = screen

        # Loads image in and gets it's and screen's rects
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Starts the ship at the bottom center of the screem
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws ship at current location"""
        self.screen.blit(self.image, self.rect)