
import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH =1000
SCREEN_HEIGHT =1000
SCREEN_TITLE = "Bouncing Rectangle Example"

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50

## put mouse listener, make sure the triagle stays on screen. and transfer data over sockets. every time it hits wall, want to create new shape, and on collision delete each other. matrix multiplication with numpy. spectral value decomposition.

def on_mouse_press(x,y,button,modifiers):
    if button == arcade.MOUSE_BUTTON_LEFT:
        val_x = x
        val_y = y
        return val_x,val_y


def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """

    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()

    # Draw a rectangle.
    # For a full list of colors see:
    # http://arcade.academy/arcade.color.html
   
    arcade.draw_triangle_filled(on_draw.center_x + 40, on_draw.center_y,
                                    on_draw.center_x, on_draw.center_y - 100,
                                    on_draw.center_x + 80, on_draw.center_y - 100,
                                    arcade.color.DARK_GREEN)

    # Modify rectangles position based on the delta
    # vector. (Delta means change. You can also think
    # of this as our speed and direction.)
    # on_draw.center_x += on_draw.delta_x
    # on_draw.center_y += on_draw.delta_y

    on_draw.center_x += on_mouse_press()[0]
    on_draw.center_y += on_mouse_press()[1]

    # Figure out if we hit the edge and need to reverse.
    if on_draw.center_x < RECT_WIDTH // 2 \
            or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
        on_draw.delta_x *= -1
    if on_draw.center_y < RECT_HEIGHT // 2 \
            or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
        on_draw.delta_y *= -1
    print(on_draw.center_x)

# Below are function-specific variables. Before we use them
# in our function, we need to give them initial values. Then
# the values will persist between function calls.
#
# In other languages, we'd declare the variables as 'static' inside the
# function to get that same functionality.
#
# Later on, we'll use 'classes' to track position and velocity for multiple
# objects.
on_draw.center_x = 100  # type: ignore # dynamic attribute on function obj  # Initial x position
on_draw.center_y = 50   # type: ignore # dynamic attribute on function obj  # Initial y position
on_draw.delta_x = 100   # type: ignore # dynamic attribute on function obj  # Initial change in x
on_draw.delta_y = 50  # type: ignore # dynamic attribute on function obj  # Initial change in y


def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw,0.1)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()