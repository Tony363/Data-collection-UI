import sys, pygame, math;
from pygame.locals import *;
spaceship = (r'C:\Users\Tony\Desktop\p01xs9fk.jpg')
mouse_c = (r'C:\Users\Tony\Desktop\cl_crosshairstyle_4.png')
backg = (r'C:\Users\Tony\Desktop\download.png')
pygame.init()
screen = pygame.display.set_mode((800, 600))
bk = pygame.image.load(backg).convert_alpha()
mousec = pygame.image.load(mouse_c).convert_alpha()
space_ship = pygame.image.load(spaceship).convert_alpha()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("test1")
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            print("test3")
    screen.blit(bk, (0, 0))
    pos = pygame.mouse.get_pos()
    screen.blit(mousec, (pos))
    angle = 360-math.atan2(pos[1]-300,pos[0]-400)*180/math.pi
    rotimage = pygame.transform.rotate(space_ship,angle)
    rect = rotimage.get_rect(center=(400,300))
    screen.blit(rotimage,rect) #I need space_ship to rotate towards my cursor
    pygame.display.update()