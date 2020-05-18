# Creating a Settings Class


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 850
        self.screen_height = 550
        self.bg_color = (230, 230, 230)
