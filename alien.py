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

    def check_edges(self):
        """Returns True if the alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves alien to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x
    

    def blitme(self):
        """Draws the alien onto the screen"""
        self.screen.blit(self.image, self.rect)


