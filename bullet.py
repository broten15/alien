import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from ship"""

    def __init__(self, screen, ai_settings, ship):
        """creates a bullet object at the ships current position"""
        super().__init__()
        self.screen = screen
    
        # Create a bullet and set it's position to ship
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullets initial position in a float
        self.y = float(self.rect.y)

        # Set attribute for the bullet
        self.bullet_color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen"""
        # Updates the position value of the bullet
        self.y -= self.bullet_speed_factor
        # Updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet at current position"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)