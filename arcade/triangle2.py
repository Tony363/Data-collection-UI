import arcade
import os
import math
import random


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

RECT_WIDTH = 700
RECT_HEIGHT = 500

SCREEN_TITLE = "Raymonds little games"

SHIP_SPEED = 5


class Shape:

    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_angle = delta_angle
        self.color = color

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        self.angle += self.delta_angle

class Rectangle(Shape):

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)

class Triangle:
    def __init__(self,val_x,val_y,color):
        self.center_x = val_x
        self.center_y = val_y
        self.color = color
        self.x = self.center_x + 40 
        self.y = self.center_y
        self.x1 = self.center_x
        self.y1 = self.center_y - 100
        self.x2 = self.center_x + 80
        self.y2 = self.center_y -100
    
    def draw(self):
        arcade.draw_triangle_filled(self.center_x + 40, self.center_y,
                                    self.center_x, self.center_y - 100,
                                    self.center_x + 80, self.center_y -100,
                                    arcade.color.WHITE)

    #If f is your angle, (x,y) becomes (xcosf−ysinf,ycosf+xsinf).



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
    
    def rotate(self):
        self.x = (math.cos(self.angle) * (self.center_x + 40)) - (math.sin(self.angle) * self.center_y)
        self.y = (math.cos(self.angle) * self.center_y) + (math.sin(self.angle) * (self.center_x + 40))

        self.x1 = (math.cos(self.angle) * self.center_x) - (math.sin(self.angle) * (self.center_y-100))
        self.y1 = (math.cos(self.angle) * self.center_y-100) + (math.sin(self.angle) * self.center_x )

        self.x2 = (math.cos(self.angle) * (self.center_x + 80)) - (math.sin(self.angle) * (self.center_y -100))
        self.y2 = (math.cos(self.angle) * self.center_y-100) + (math.sin(self.angle) * (self.center_x + 80))


       



          
          
       
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

        self.shape_list = None
        self.triangle_list = None

        self.triangle_table = {}
        self.val_x = 700
        self.val_y = 500
    

        self.triangle = Triangle(self.val_x,self.val_y,arcade.color.WHITE)

        self.count = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.shape_list = []
        self.triangle_list = []

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawingtracking_table
        arcade.start_render()

        self.triangle.draw()
        
        for shape in self.shape_list:
            shape.draw()
        
        # for triangle in self.triangle_list:
        #     triangle.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        x = random.randrange(0, SCREEN_WIDTH)
        y = random.randrange(0, SCREEN_HEIGHT)
        width = random.randrange(10, 30)
        height = random.randrange(10, 30)
        angle = random.randrange(0, 360)

        d_x = random.randrange(-3, 4)
        d_y = random.randrange(-3, 4)
        d_angle = random.randrange(-3, 4)

        red = random.randrange(256)
        green = random.randrange(256)
        blue = random.randrange(256)
        alpha = random.randrange(256)

        shape_type = random.randrange(2)

        self.triangle.triangle_follow(self.val_x,self.val_y)

        
        hit_list = [(shape.x,shape.y) for shape in self.shape_list]

        for hit in self.shape_list: 

            if (int(self.triangle.center_x) in range(hit.x-50,hit.x+50)) and (int(self.triangle.center_y) in range(hit.y-50,hit.y+50)):
                self.shape_list.remove(hit)


        if  self.triangle.center_x < 50:
            self.triangle.center_x += 50

        elif self.triangle.center_x > SCREEN_WIDTH-50:
            self.triangle.center_x -= 50
        
        if self.triangle.center_y > SCREEN_HEIGHT-50:
            self.triangle.center_y -= 50
        
        elif self.triangle.center_y < 50:
            self.triangle.center_y += 50

        if len(self.shape_list) < 50:

            if (self.triangle.center_x < SCREEN_WIDTH//10 and self.triangle.center_x > 0) or (self.triangle.center_x > SCREEN_WIDTH - SCREEN_WIDTH//10  and self.triangle.center_x < SCREEN_WIDTH):

                shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                    d_angle, (red, green, blue, alpha))
                self.shape_list.append(shape)

            if (self.triangle.center_y < SCREEN_HEIGHT//10 and self.triangle.center_y > 0) or (self.triangle.center_y > SCREEN_HEIGHT - SCREEN_HEIGHT//10 and self.triangle.center_y < SCREEN_HEIGHT):

                shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                    d_angle, (red, green, blue, alpha))
                self.shape_list.append(shape)
            
         

    def on_mouse_press(self,x,y,button,modifiers):
        
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.count += 1
            self.val_x = x
            self.val_y = y
            # self.triangle.rotate()
       

            for count in range(self.count):
                if f'coor {self.count}' not in self.triangle_table: 
                    self.triangle_table[f'coor {self.count}'] = self.val_x,self.val_y
                elif f'coor {self.count}' in self.triangle_table:
                    continue
        
            
    
    def get_table(self):
        print(self.triangle_table)
        return self.triangle_table

   
def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
    window.get_table()


if __name__ == "__main__":
    main()