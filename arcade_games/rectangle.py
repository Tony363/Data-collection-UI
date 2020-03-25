import arcade

class Rectangle:
    """
    Define Rectangle object that inherits our base Shape Object. 
    This Rectangle object is created when our triangle gets near 
    to the wall of our screen
    """
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
    # define a move method for our Shapes
    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        self.angle += self.delta_angle

    # One method of drawing a rectangle is sufficient
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)

## make simple rectangle instance example

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    
        arcade.set_background_color(arcade.color.WHITE)

        self.rectangle = Rectangle(100,100,100,100,100,100,100,100,arcade.color.BLACK)


    def on_draw(self):
        arcade.start_render()

        self.rectangle.draw()


def main():
    window = MyGame(500,500,'simple')
    arcade.run()

if __name__ == "__main__":
    main()

