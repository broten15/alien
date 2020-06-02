class Settings():
    """A class to store the settings for Alien invasion"""

    def __init__(self):
        """Initializes game settings"""
        # Screen setings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.5
