import math
import pygame as pg
from pygame.math import Vector2


pg.init()
screen = pg.display.set_mode((640, 480))
FONT = pg.font.Font(None, 24)
BLACK = pg.Color('black')
BULLET_IMAGE = pg.Surface((20, 11), pg.SRCALPHA)
pg.draw.polygon(BULLET_IMAGE, pg.Color('grey11'), [(0, 0), (20, 5), (0, 11)])


def update_bullets(bullets):
    """Add the velocity to the pos then assign pos to the rect center."""
    for bullet_rect, pos, velocity, _ in bullets:
        pos[0] += velocity[0]
        pos[1] += velocity[1]
        bullet_rect.center = pos


def draw_bullets(bullets, screen):
    for bullet_rect, pos, _, image in bullets:
        screen.blit(image, bullet_rect)
        pg.draw.rect(screen, (200, 140, 0), bullet_rect, 1)


def main():
    clock = pg.time.Clock()
    # The cannon image and rect.
    cannon_img = pg.Surface((60, 22), pg.SRCALPHA)
    pg.draw.rect(cannon_img, pg.Color('grey19'), [0, 0, 35, 22])
    pg.draw.rect(cannon_img, pg.Color('grey19'), [35, 6, 35, 10])
    orig_cannon_img = cannon_img  # Store orig image to preserve quality.
    cannon = cannon_img.get_rect(center=(320, 240))
    angle = 0  # Angle of the cannon.

    # Add bullets to this list. Bullets will also be lists
    # consisting of a pygame.Rect, the velocity and the image.
    bullets = []
    bullet_speed = 5

    playing = True
    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Left button fires a bullet from cannon center with
                # current angle. Add the bullet to the bullets list.
                if event.button == 1:
                    # Use cosine and sine to calculate the x and y
                    # velocity. Scale them by the desired speed.
                    velocity = (math.cos(math.radians(angle)) * bullet_speed,
                                math.sin(math.radians(angle)) * bullet_speed)
                    img = pg.transform.rotate(BULLET_IMAGE, -angle)
                    bullet_rect = img.get_rect(center=cannon.center)
                    # The extra pos list is needed because the pygame.Rect
                    # can only have ints as the x and y value. We still
                    # need the rect for collision detection.
                    pos = list(bullet_rect.center)
                    bullet = [bullet_rect, pos, velocity, img]
                    bullets.append(bullet)

        update_bullets(bullets)
        # Find angle to target (mouse pos).
        x, y = Vector2(pg.mouse.get_pos()) - cannon.center
        angle = math.degrees(math.atan2(y, x))
        # Rotate the cannon image.
        cannon_img = pg.transform.rotate(orig_cannon_img, -angle)
        cannon = cannon_img.get_rect(center=cannon.center)

        # Draw
        screen.fill(pg.Color('darkseagreen4'))
        draw_bullets(bullets, screen)
        screen.blit(cannon_img, cannon)
        txt = FONT.render('angle {:.1f}'.format(angle), True, BLACK)
        screen.blit(txt, (10, 10))
        pg.draw.line(
            screen, pg.Color(150, 60, 20),
            cannon.center, pg.mouse.get_pos(), 2)
        pg.display.update()

        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()