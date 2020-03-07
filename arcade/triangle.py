import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing With Functions Example"


# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()


def triangle(x,y):
    arcade.draw_triangle_filled(center_x + 40, center_y,
                                    center_x, center_y - 100,
                                    center_x + 80, center_y - 100,
                                    arcade.color.DARK_GREEN)

triangle(50,250)

# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
