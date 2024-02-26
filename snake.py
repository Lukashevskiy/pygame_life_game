import pygame as pg
from src.constants import *
from src.cell import Cell, create_group_field
from src.field import *

pg.init()

main_screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()

field_ = create_field(N, M)
field = create_group_field(N, M)

dx, dy = 1, 0
snake = [[N//2, M//2]]

last_time = 0
speed = 200
game_over = False
is_running = True
while is_running:
    time_delta = clock.tick(FPS)
    last_time += time_delta

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if game_over:
                break

            if event.key == pg.K_UP:
                dy = -1
                dx = 0
            if event.key == pg.K_DOWN:
                dy = 1
                dx = 0
            if event.key == pg.K_LEFT:
                dx = -1
                dy = 0
            if event.key == pg.K_RIGHT:
                dx = 1
                dy = 0

    if last_time > speed:
        last_time = 0
        speed -= 10
        y, x = snake[-1]
        field_[y][x] = 0

        y, x = snake[0]
        y += dy
        x += dx

        if y == 1:
            y = N
        if x == 1:
            x = M
        if y == N:
            y = 1
        if x == M:
            x = 1

        snake.insert(0, (y, x))
        field_[y][x] = 1

        snake.pop()

    field.update(field_, colors)
    main_screen.fill(COLORS['black'])
    field.draw(main_screen)

    pg.display.flip()