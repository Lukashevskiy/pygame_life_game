import pygame as pg
from src.constants import C_HEIGHT, C_WIDTH, MURDER_C, ALIVE_C

class Cell(pg.sprite.Sprite):

    def __init__(self, position, state, i, j):
        super().__init__()
        self.i = i
        self.j = j
        self.color = state
        self.image = pg.Surface((C_WIDTH-0.1, C_HEIGHT-0.1))
        self.rect  = self.image.get_rect()
        self.rect.topleft = position

    def update(self, field_, colors):
        state = field_[self.i][self.j]
        self.color = colors[state]
        
        self.image.fill(self.color)

def create_group_field(n, m):
    field = pg.sprite.Group()

    for i in range(n):
        for j in range(m):
            Cell(
                position=(C_WIDTH * j, C_HEIGHT * i), 
                state=0,
                i=i+1,
                j=j+1
            ).add(field)
    
    return field