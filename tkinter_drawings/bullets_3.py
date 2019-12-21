import pygame
import random
import time
import math
import sys

pygame.init()

#The size of the game window
display_width = 1280
display_height = 800

#Colors available
black = (0, 0, 0) #colours defined by RGB,
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 150, 0)
bright_red = (255, 0, 0)
bright_green =(0, 255, 0)

#This code opens up the Game window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Blockslayer")
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

#player character info
slayerImg = pygame.image.load(r'C:\Users\Tony\Desktop\cl_crosshairstyle_4.png').convert_alpha()
slayerWidth = 84
slayerHeight = 84


#mouse info
mouse_c = pygame.image.load(r'C:\Users\Tony\Desktop\cl_crosshairstyle_4.png').convert_alpha()

def crosshair(mousex,mousey):
   mousex, mousey = pygame.mouse.get_pos()
   small_ch = pygame.transform.scale(mouse_c, (20, 20))
   gameDisplay.blit(small_ch, (mousex, mousey,))

   print(mousex,mousey)

#player character
def slayer(x,y,):
    #small_slayer = pygame.transform.scale(slayerImg, (120, 80,))
    pos_x,pos_y = pygame.mouse.get_pos()
    run, rise = (pos_x - x, pos_y - y)
    angle = math.degrees(math.atan2(rise, run))
    
    rotimage = pygame.transform.rotate((slayerImg), -angle,)
    rect = rotimage.get_rect(center=(x, y))
    gameDisplay.blit(rotimage, rect,)
    pygame.display.update()

# def rotate(x, y, mouse_pos, image):
#     # Calculate x and y distances to the mouse pos.
#     run, rise = (mouse_pos[0]-x, mouse_pos[1]-y)
#     # Pass the rise and run to atan2 (in this order)
#     # and convert the angle to degrees.
#     angle = math.degrees(math.atan2(rise, run))
#     # Rotate the image (use the negative angle).
#     rotimage = pygame.transform.rotate(image, -angle)
#     rect = rotimage.get_rect(center=(x, y))
#     return rotimage, rect

#Game Logic
def block_game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    pos = pygame.mouse.get_pos()
    angle = 360 - math.atan2(pos[1] + x - 84, pos[0] + y - 84) * 180 / math.pi
    rotimage = pygame.transform.rotate((slayerImg), angle,)

    mousex, mousey = pygame.mouse.get_pos()


    #def blockguy(blockguyX, blockguyY, blockguyW, blockguyH, ):
    #blockguyX = random.randrange(0, 785)
    #blockguyY = random.randrange (0, 600)
    #blockguyW = 166
    #blockguyH = 110
    #blockguy_speed = 5


    #Event handler
    exit_game = False

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_s]: y += 7
        if pressed[pygame.K_w]: y -= 7
        if pressed[pygame.K_a]: x -= 7
        if pressed[pygame.K_d]: x += 7





        gameDisplay.fill(white)
        slayer(x, y,)

        #Boundaries
        if x > display_width:
            x = 1275

        if x < 0:
            x = 5

        if y > display_height:
            y = 795

        if y < 0:
            y = 5

        crosshair(mousex,mousey)
        #blockguy(blockguyX, blockguyY, blockguyW, blockguyH, )
        pygame.display.update()
        clock.tick(60)


block_game_loop()
pygame.quit()
quit()