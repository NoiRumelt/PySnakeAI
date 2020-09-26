import pygame as pg

pg.init()
screen = pg.display.set_mode((300,300))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    clock.tick(5)
    pg.display.update()
