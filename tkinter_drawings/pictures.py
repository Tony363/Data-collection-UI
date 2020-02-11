# experiments with module pygame, free from: http://www.pygame.org/
# move an image rectangle to follow the mouse click position (ulc)
# tested with Python25 and PyGame18     vegaseat     07aug2008
import pygame as pg
import math

# initialize pygame
pg.init()

# use an image you have (.bmp  .jpg  .png  .gif)
spaceship = (r'/home/tony/Downloads/bullet.jpeg')
mouse_c = (r'/home/tony/Downloads/crosshair.png')
backg = (r'/home/tony/Downloads/black_background.jpeg')


# give the screen a title
pg.display.set_caption('image follows mouse click position')

# screen size
screen = pg.display.set_mode((800, 600))

# load background
bk = pg.image.load(backg).convert_alpha()
# load mouse image
mousec = pg.image.load(mouse_c).convert_alpha()
# load space ship
space_ship = pg.image.load(spaceship).convert_alpha()


# set mouse to visable
pg.mouse.set_visible(True)
# display spaceship image
start_rect = space_ship.get_rect()
image_rect = start_rect


matrix = []
running = True
while running:

    # watch for user inputs
    event = pg.event.poll()
    # watch for user keyboard inputs
    keyinput = pg.key.get_pressed()
 

    # exit on corner 'x' click or escape key press
    if keyinput[pg.K_ESCAPE]:
        print(matrix)
        raise SystemExit
    elif event.type == pg.QUIT:
        running = False
    elif event.type == pg.MOUSEBUTTONDOWN:
        
        # test
        mouse_loc = "mouse click at [%d, %d]" % event.pos
        
        # display caption as mouse location
        pg.display.set_caption(mouse_loc)
        mouse_pos = list(event.pos)
        matrix.append(mouse_pos)

        # move space ship to mouse location
        image_rect = start_rect.move(mouse_pos)
        """
        print image_rect  # test
        print "corner coordinates --> (%d, %d, %d, %d)" % \
            (image_rect.left, image_rect.top, image_rect.right,
            image_rect.bottom)
        """

    # set black background 
    screen.blit(bk,(0,0))
    # get mouse position
    pos = pg.mouse.get_pos()
    
    # change screen according to mouse movement
    screen.blit(mousec,(pos))

    # calculating angle change relative to mouse
    angle = 360-math.atan2(pos[1]-300,pos[0]-400)*180/math.pi
 
    # transform by rotation of space ship
    rotimage = pg.transform.rotate(space_ship,angle)
    rect = rotimage.get_rect()
    print(pos,angle)

    # update screen
    screen.fill((0,0,0))
    screen.blit(rotimage, image_rect)
    pg.display.update()


    #### https://www.daniweb.com/programming/software-development/code/217116/image-follows-mouse-click-position-pygame