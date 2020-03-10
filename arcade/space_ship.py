	

"""
Move Sprite by Angle

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_angle
"""
import random
import arcade
import os
import math
import sys
import time
from math import sqrt

SPRITE_SCALING = 1
SPRITE_SCALING_COIN = 0.5
SPRITE_SCALING_LASER = 0.8

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

SCREEN_TITLE = "run for your life"

MOVEMENT_SPEED = 6
ANGLE_SPEED = 5
BULLET_SPEED = 10
SHIP_SPEED = 4
COIN_COUNT = 0
COIN_SPEED = 1

class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """
    def __init__(self,image,scale):
        super().__init__(image, scale)
        self.coor_hist = []
     

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y
        self.coor_hist.append([self.center_x,self.center_y])


        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * COIN_SPEED
            self.change_y = math.sin(angle) * COIN_SPEED

    def get_coor(self):
        return self.coor_hist
 


class Player(arcade.Sprite):
    """ Player class """

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)



    def follow_mouse(self,val_x,val_y):

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

            # angle = 360-math.atan2(dest_x-300,dest_y-400)*180/math.pi

            # self.angle = angle
        except Exception as e:
            pass




class Triangle:
    def __init__(self,val_x,val_y,color):
        self.center_x = val_x
        self.center_y = val_y
        self.color = color
    
    def draw(self):
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

        self.tracking_table = {}

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")


        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.val_x = None
        self.val_y = None

        # self.triangle = Triangle(50,50,arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0

        # Set up the player
        self.player_sprite = Player(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

           # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            # coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            coin = Coin(':resources:images/space_shooter/meteorGrey_big3.png',SPRITE_SCALING_COIN)
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        # self.triangle.draw()

        # Put the text on the screen.
        output = f"Damage: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if self.score == 5:
            print(self.tracking_table)
            time.sleep(1)
            print('you fucked up')
            time.sleep(1)
            # return self.tracking_table
            sys.exit()

   
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
      
        self.player_list.update()
        self.bullet_list.update()
        # self.triangle.triangle_follow(self.val_x,self.val_y)
        # self.move_sprite()

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet,self.coin_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for coin in hit_list:
                coin.remove_from_sprite_lists()
                
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

        for sprite in self.player_list:
            sprite.follow_mouse(self.val_x,self.val_y)


        for i,coin in enumerate(self.coin_list):
            coin.follow_sprite(self.player_sprite)
            
            self.tracking_table[f'coin {i}'] = coin.get_coor()
            # print(f'{i} coin {self.coin_list._get_center()}')
           
        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.kill()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

            # Forward/back
        if key == arcade.key.UP:
            self.player_sprite.speed = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.speed = -MOVEMENT_SPEED

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.val_x = None
            self.player_sprite.change_angle = ANGLE_SPEED
           
        elif key == arcade.key.RIGHT:
            self.val_y = None
            self.player_sprite.change_angle = -ANGLE_SPEED

    def on_mouse_press(self,x,y,button,modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.val_x = x
            self.val_y = y

        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y

        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff,x_diff)

        bullet.angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.bullet_list.append(bullet)
     
   
    def on_mouse_motion(self,x,y,dx,dy):
        
        print(x,y)
        angle = 360-math.atan2(y-300,x-400)*480/math.pi

        # dest_x = x
        # dest_y = y

        # start_x = self.player_sprite.center_x
        # start_y = self.player_sprite.center_y

        # # Do math to calculate how to get the bullet to the destination.
        # # Calculation the angle in radians between the start points
        # # and end points. This is the angle the bullet will travel.
        # x_diff = dest_x - start_x
        # y_diff = dest_y - start_y
        # angle = math.atan2(y_diff, x_diff)

        self.player_sprite.angle = angle

    # def on_mouse_motion(self,x,y,dx,dy):

    #     self.val_x = x
    #     self.val_y = y

    # def move_sprite(self):

    #     x_dist = self.val_x - self.player_sprite._get_position()[0]
    #     y_dist = self.val_y - self.player_sprite._get_position()[1]

    #     distance = sqrt(x_dist * x_dist + y_dist * y_dist)

    #     if distance > 1:
    #         self.player_sprite.center_x += x_dist * 0.1
    #         self.player_sprite.center_y += y_dist * 0.1

    ########################################


 
               
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
    
    def get_table(self):
        print(self.tracking_table)
        return self.tracking_table  


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
    window.get_table()

    


if __name__ == "__main__":
    main()
