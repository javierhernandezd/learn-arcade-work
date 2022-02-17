"""
This is a sample program to show how to draw using the Python programming
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

# Draw background flag
arcade.draw_rectangle_filled(WIDTH, HEIGHT//2, WIDTH, 150, arcade.color.RED)
arcade.draw_rectangle_filled(WIDTH, HEIGHT//2 - 150, WIDTH, 150, arcade.color.YELLOW)
arcade.draw_rectangle_filled(WIDTH, HEIGHT//2 - 250, WIDTH, 150, arcade.color.RED)

arcade.draw_rectangle_filled(0, HEIGHT//2, WIDTH, 150, arcade.color.WHITE)
arcade.draw_rectangle_filled(0, HEIGHT//2 - 150, WIDTH, 150, arcade.color.BLUE)
arcade.draw_rectangle_filled(0, HEIGHT//2 - 250, WIDTH, 150, arcade.color.RED)

# Draw Image
texture = arcade.load_texture("images/hasbulla.png")
arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, texture.width, texture.height, texture, 0)

# Drawing Text
arcade.draw_text("HASBULLA", 0, HEIGHT - 585, arcade.color.WHITE, 80, width=WIDTH, align="center", bold=True, font_name="Kenney Future")

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
