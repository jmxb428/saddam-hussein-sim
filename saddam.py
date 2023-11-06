# rotation code is a modified version stack overflow answer 15098900
import pygame as pg
from time import time
start_time = time()
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, "assets\\", relative_path)

pg.init()
pg.mixer.music.load(resource_path("music.mp3"))
pg.mixer.music.play()
font = pg.font.SysFont(pg.font.get_default_font(),64)
text1 = font.render("WASD to move",True,(0,0,0))
text2 = font.render("Q/E to rotate",True,(0,0,0))
text3 = font.render("ESC to exit",True,(0,0,0))
pg.display.set_caption('Sadam Hussein Simulator')

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pg.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

pg.init()
screen = pg.display.set_mode()
HIDEOUT = pg.image.load(resource_path("back.jpg"))
# The original image will never be modified.
IMAGE = pg.image.load(resource_path("saddamsp.png"))
# Store the original center position of the surface.
pivot = [200, 250]
# This offset vector will be added to the pivot point, so the
# resulting rect will be blitted at `rect.topleft + offset`.
offset = pg.math.Vector2(0, 0)
angle = 0

running = True
while running:
    actualTime = f"{int(time()-start_time)//60}:{round((time()-start_time)%60,3)}"
    speed = font.render(actualTime,True,(0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_e]:
                angle += 10
            elif keys[pg.K_q]:
                angle -= 10
            if keys[pg.K_d]:
                pivot[0] += 10
            elif keys[pg.K_a]:
                pivot[0] -= 10
            elif keys[pg.K_s]:
                pivot[1] += 10
            elif keys[pg.K_w]:
                pivot[1] -= 10
            if keys[pg.K_ESCAPE]:
                pg.quit()


    # Rotated version of the image and the shifted rect.
    rotated_image, rect = rotate(IMAGE, angle, pivot, offset)

    # Drawing.
    screen.blit(HIDEOUT,(0,0))
    screen.blit(rotated_image, rect)  # Blit the rotated image.
    pg.draw.circle(screen, (30, 250, 70), pivot, 3)  # Pivot point.
    screen.blit(text1,(16,screen.get_height()-128))
    screen.blit(text2,(16,screen.get_height()-64))
    screen.blit(text3,(screen.get_width()-256,screen.get_height()-64))
    screen.blit(speed,(0,0))
    if pivot[0] > 900 and pivot[0] < 1000 and pivot[1] > 650 and pivot[1] < 750 and angle == -90:
        running = False
    pg.display.flip()

floopyDoop = font.render(actualTime,True,(0,0,0))
gleepGlorp = pg.image.load(resource_path("win.jpg"))
screen.blit(gleepGlorp,(0,0))
shloopFroop = pg.Rect(screen.get_width()/2 - floopyDoop.get_width()/2 -5, screen.get_height()/2-5,floopyDoop.get_width()+10,floopyDoop.get_height()+5)
pg.draw.rect(screen, (255,255,255), shloopFroop, 0, 10)
screen.blit(floopyDoop,(screen.get_width()/2 - floopyDoop.get_width()/2,screen.get_height()/2))
pg.display.flip()

run2 = True
while run2:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run2 = False
        if event.type == pg.KEYDOWN:
            grouble = pg.key.get_pressed()
            if grouble[pg.K_ESCAPE]:
                run2 = False

pg.quit()