import arcade
import os
import math


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

RECT_WIDTH = 700
RECT_HEIGHT = 500

SCREEN_TITLE = "Raymonds little games"

SHIP_SPEED = 5




class Triangle:
    def __init__(self,val_x,val_y,color):
        self.center_x = val_x
        self.center_y = val_y
        self.color = color
    
    def draw(self,center_x,center_y):
        arcade.draw_triangle_filled(self.center_x + 40, self.center_y,
                                    self.center_x, self.center_y - 100,
                                    self.center_x + 80, self.center_y - 100,
                                    arcade.color.WHITE)


    def triangle_follow(self,val_x,val_y):

        start_x = self.center_x
        start_y = self.center_y

        # Get the destination location for the bullet
        try:
            dest_x = val_x
            dest_y = val_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * SHIP_SPEED
            self.change_y = math.sin(angle) * SHIP_SPEED

            self.center_x += self.change_x
            self.center_y += self.change_y

            angle = 360-math.atan2(dest_x-300,dest_y-400)*180/math.pi

            self.angle = angle
        except Exception as e:
            print('error')
            pass
          
          
       
class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.triangle_list = []
        self.val_x = 700
        self.val_y = 500
    

        self.triangle = Triangle(500,500,arcade.color.WHITE)

    # def setup(self):
    #     """ Set up the game and initialize the variables. """

    #     # Sprite lists
        

    #     self.triangle_list = arcade.SpriteList()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawingtracking_table
        arcade.start_render()

        self.triangle.draw(500,500)


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        self.triangle.triangle_follow(self.val_x,self.val_y)
       
        if self.triangle.center_x > SCREEN_WIDTH//2:
            print('crossed')
            self.triangle.draw(self.val_x,self.val_y)

        if self.triangle.center_y > SCREEN_HEIGHT//2:
            print('crossed')
            self.triangle.draw(self.val_x,self.val_y)

    def on_mouse_press(self,x,y,button,modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.val_x = x
            self.val_y = y
            # print(self.val_x,self.val_y)

   
def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # window.setup()
    arcade.run()
    # window.get_table()


if __name__ == "__main__":
    main()