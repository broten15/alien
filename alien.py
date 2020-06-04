import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in it's fleet"""

    def __init__(self, ai_settings, screen):
        """Initializes the alien and sets it's initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
    
        # Loads image in and gets it's rect
        self.image = pygame.image.load('images\\alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the x position as a float
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the alien onto the screen"""
        self.screen.blit(self.image, self.rect)


