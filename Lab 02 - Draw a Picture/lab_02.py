""" This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Global Variables
WIDTH = 800
HEIGHT = 600
WINDOW_TITLE = "Drawing Example"

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(WIDTH, HEIGHT, WINDOW_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BABY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw circle in the middle of the screen
arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, 250, 250, arcade.color.WHITE)

# Draw Twitter Image
texture = arcade.load_texture("images/Twitter.png")
arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, texture.width - 980, texture.height - 790, texture, 0)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
