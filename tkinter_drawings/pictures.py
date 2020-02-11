# experiments with module pygame, free from: http://www.pygame.org/
# move an image rectangle to follow the mouse click position (ulc)
# tested with Python25 and PyGame18     vegaseat     07aug2008
import pygame as pg
import math
# initialize pygame
pg.init()
# use an image you have (.bmp  .jpg  .png  .gif)
# image_file = r"C:\Users\Tony\Desktop\800px_COLOURBOX3347559.jpg"
spaceship = (r'/home/tony/Downloads/bullet.jpeg')
mouse_c = (r'/home/tony/Downloads/crosshair.png')
backg = (r'/home/tony/Downloads/black_background.jpeg')


# give the screen a title
pg.display.set_caption('image follows mouse click position')

screen = pg.display.set_mode((800, 600))
bk = pg.image.load(backg).convert_alpha()
mousec = pg.image.load(mouse_c).convert_alpha()
space_ship = pg.image.load(spaceship).convert_alpha()
clock = pg.time.Clock()
pg.mouse.set_visible(True)
start_rect = space_ship.get_rect()
image_rect = start_rect
running = True


while running:
  
    event = pg.event.poll()
    keyinput = pg.key.get_pressed()
 
    # exit on corner 'x' click or escape key press
    if keyinput[pg.K_ESCAPE]:
        raise SystemExit
    elif event.type == pg.QUIT:
        running = False
    elif event.type == pg.MOUSEBUTTONDOWN:
        
        print (event.pos, list(event.pos))  # test
        mouse_loc = "mouse click at (%d, %d)" % event.pos
        pg.display.set_caption(mouse_loc)
        mouse_pos = list(event.pos)
        image_rect = start_rect.move(mouse_pos)
        """
        print image_rect  # test
        print "corner coordinates --> (%d, %d, %d, %d)" % \
            (image_rect.left, image_rect.top, image_rect.right,
            image_rect.bottom)
        """
       
    screen.blit(bk,(0,0))
    pos = pg.mouse.get_pos()
    screen.blit(mousec,(pos))
    angle = 360-math.atan2(pos[1]-300,pos[0]-400*180/math.pi)
    rotimage = pg.transform.rotate(space_ship,angle)
    rect = rotimage.get_rect(center=(400,300))
    screen.blit(rotimage, rect)
    # pg.display.update()
    # this erases the old sreen with black
   
    # put the image on the screen
    
    # update screen
    screen.fill((0,0,0))
    screen.blit(space_ship, image_rect)
    pg.display.flip()
    # clock.tick(30)


    #### https://www.daniweb.com/programming/software-development/code/217116/image-follows-mouse-click-position-pygame