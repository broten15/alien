class GameStats():
    """Tracks statistics for alien invasion"""

    def __init__(self, ai_settings):
        """Initializes statistics"""
        self.ai_settings = ai_settings
        self.reset_settings()

        # Start alien invasion in an active state
        self.game_active = True
    
    def reset_settings(self):
        """Initializes statistics that can change during game"""
        self.ships_left = self.ai_settings.ship_limit