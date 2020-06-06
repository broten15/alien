filename = 'high_score.txt'
with open(filename, 'r') as f_obj:
    high_score_number = int(f_obj.read())
    
class GameStats():
    """Tracks statistics for alien invasion"""

    def __init__(self, ai_settings):
        """Initializes statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = high_score_number

        # Start alien invasion in an active state
        self.game_active = False
    
    def reset_stats(self):
        """Initializes statistics that can change during game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1