import pygame as pg
from src.constants import C_HEIGHT, C_WIDTH, MURDER_C, ALIVE_C

class Cell(pg.sprite.Sprite):

    def __init__(self, position, state, i, j):
        super().__init__()
        self.i = i
        self.j = j
        self.state = state
        self.image = pg.Surface((C_WIDTH-0.1, C_HEIGHT-0.1))
        self.rect  = self.image.get_rect()
        self.rect.topleft = position

    def update(self, field_):
        self.state = field_[self.i][self.j]
        color = MURDER_C
        if self.state == 1:
            color = ALIVE_C

        self.image.fill(color)
