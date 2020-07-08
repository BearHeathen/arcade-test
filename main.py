# IMPORTS
import arcadeplus as arcade
import random

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
RADIUS = 150

# CLASSES

class Welcome(arcade.Window):
    """Main welcome window"""
    def __init__(self):
        """Initialize the window"""

        # Call parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        """Called when you need to draw your window"""

        """Clear screen and start drawing"""
        arcade.start_render()

        """Draw a blue circle"""
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.ALIZARIN_CRIMSON
        )


# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    arcade.run()