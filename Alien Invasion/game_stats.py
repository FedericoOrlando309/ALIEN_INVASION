class GameStats():
    """Track statistics fopr alien Invasion"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # start alien invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit