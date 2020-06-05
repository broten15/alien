class Settings():
    """A class to store the settings for Alien invasion"""

    def __init__(self):
        """Initializes static game settings"""
        # Screen setings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 6

        # Alien settings
        self.fleet_drop_speed = 25

        # How quickly the game speeds up
        self.speedup_scale = 2

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initializes dynamic settings throughout game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1

        # Fleet direction of 1=right; -1=left
        self.fleet_direction = 1

    def speedup_game(self):
        """Speed up game after fleet is shot down"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
