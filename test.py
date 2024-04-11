import pygame as pg
import sys
pg.init()
from pygame_button import Button

sc = pg.display.set_mode((400, 300))
sc.fill((200, 255, 200))


b1 = Button(20, 20, 20)
b2 = Button()


font = pg.font.Font(None, 72)
text = font.render("Hello Wold", True, (0, 100, 0))
place = text.get_rect(center=(200, 150))
sc.blit(text, place)

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:
        place.x -= 1
    elif pressed[pg.K_RIGHT]:
        place.x += 1

    sc.fill((200, 255, 200))
    sc.blit(text, place)

    pg.display.update()

    pg.time.delay(20)