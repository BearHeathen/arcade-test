# IMPORTS
from typing import Optional

import arcadeplus as arcade
import random

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Raven Shooter"
SCALING = 0.15



# CLASSES

class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites.
        Flying sprites include enemies and clouds"""

    def update(self):
        """Update the sprite's position when it moves off-screen to the left"""

        # Move the sprite
        super().update()

        # Remove if off-screen
        if self.right < 0:
            self.remove_from_sprite_lists()


class RavenShooter(arcade.Window):
    """Space Shooter side scroller game.
       Player starts on left, enemies appear on the right.
       Player can move anywhere except off-screen.
       Enemies fly to the left at variable speeds.
       Collisions end game. """

    def __init__(self):
        """ Initialize the game"""

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList(use_spatial_hash=True)

        self.setup()

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()

    def on_update(self, delta_time: float):
        """ Update the positions and statuses of all game objects. If paused, do nothing"""

        # If paused, do nothing
        if self.paused:
            return

        # Update everything
        self.all_sprites.update()

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def setup(self):
        """ Get the game ready to play"""
        self.paused = False
        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set up the player
        self.player = arcade.Sprite("images/raven.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)

        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_enemy, 0.25)

        # Spawn a new cloud every second
        arcade.schedule(self.add_cloud, 1.0)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time{float} --> How much time has passed
            since the last call
        """
        # First, create the new enemy sprite
        enemy = FlyingSprite("images/attack-bird.png", SCALING)

        # Set its position to a random height and off screen-right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-20, 5), 0)

        # Add it to the enemies list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def add_cloud(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time{float} --> How much time has passed
            since the last call
        """
        # First, create the new cloud sprite
        cloud = FlyingSprite("images/cloud.png", SCALING)

        # Set its position to a random height and off screen-right
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        cloud.velocity = (random.randint(-5, -2), 0)

        # Add it to the enemies list
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)

    def on_key_press(self, symbol, modifiers):
        """ Handle user keyboard input
            Q: Quit
            P: Pause
            W/A/S/D: Move Up, Left, Down, Right

            Arguments:
                symbol{int} --> Which key was pressed
                modifiers{int} --> Which modifiers were pressed"""

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.change_y = 5

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player.change_y = -5

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -5

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} --> Which key was pressed
            modifiers {int} --> Which modifiers were pressed
        """
        if (
                symbol == arcade.key.W
                or symbol == arcade.key.S
                or symbol == arcade.key.UP
                or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
                symbol == arcade.key.A
                or symbol == arcade.key.D
                or symbol == arcade.key.LEFT
                or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

# Main entry
if __name__ == "__main__":
    app = RavenShooter()
    arcade.run()
