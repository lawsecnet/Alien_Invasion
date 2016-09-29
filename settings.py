class Settings():

    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 0, 0
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        # fleet directiom; 1 represeents right, -1 represents left
        self.fleet_direction = 1
