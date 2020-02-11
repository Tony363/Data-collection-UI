import math
import pygame


pygame.init()

gray = (30, 30, 30)

display_width, display_height = (1280, 800)
gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

slayerImg = pygame.Surface((104, 84), pygame.SRCALPHA)
pygame.draw.polygon(slayerImg, (0, 120, 250), [(1, 1), (103, 42), (1, 83)])


def rotate(x, y, mouse_pos, image):
    # Calculate x and y distances to the mouse pos.
    run, rise = (mouse_pos[0]-x, mouse_pos[1]-y)
    # Pass the rise and run to atan2 (in this order)
    # and convert the angle to degrees.
    angle = math.degrees(math.atan2(rise, run))
    # Rotate the image (use the negative angle).
    rotimage = pygame.transform.rotate(image, -angle)
    rect = rotimage.get_rect(center=(x, y))
    return rotimage, rect


def block_game_loop():
    x = display_width * 0.45
    y = display_height * 0.8

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]: y += 7
        if pressed[pygame.K_w]: y -= 7
        if pressed[pygame.K_a]: x -= 7
        if pressed[pygame.K_d]: x += 7

        mousex, mousey = pygame.mouse.get_pos()
        # Boundaries
        if x > display_width:
            x = 1275
        if x < 0:
            x = 5
        if y > display_height:
            y = 795
        if y < 0:
            y = 5

        gameDisplay.fill(gray)
        rotimage, rect = rotate(x, y, (mousex, mousey), slayerImg)
        gameDisplay.blit(rotimage, rect)

        pygame.display.update()
        clock.tick(60)


block_game_loop()
pygame.quit()