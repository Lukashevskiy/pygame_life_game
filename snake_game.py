import pygame as pg
from src.constants import *
from src.cell import Cell, create_group_field
from src.field import *
from src.snake import *
import random
pg.init()

main_screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()

field_ = create_field(N, M)
field = create_group_field(N, M)


snake = Snake(position=[N//2, M//2], direction=[1, 0])
snake.body.append([N//2 + 1, M//2 + 1])
snake.body.append([N//2 + 2, M//2 + 2])

def generate_apple(snake_body, n, m):
    position = (random.randint(1, n+1), random.randint(1, m+1))
    while position in snake_body:
        position = (random.randint(1, n+1), random.randint(1, m+1))

    return position


apple_position = generate_apple(snake.body, N, M)
field_[apple_position[0]][apple_position[1]] = 2


last_time = 0
speed = 100
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
                if snake.direction != [1, 0]:
                    snake.direction = [-1, 0]

            if event.key == pg.K_DOWN:
                if snake.direction != [-1, 0]:
                    snake.direction = [1, 0]

            if event.key == pg.K_LEFT:
                if snake.direction != [0, 1]:
                    snake.direction = [0, -1]

            if event.key == pg.K_RIGHT:
                if snake.direction!= [0, -1]:
                    snake.direction = [0, 1]


    if last_time >= speed:
        last_time = 0
        delete_tale = True
        head_position = snake.body[0]
        
        if head_position == apple_position:
            delete_tale = False
        
        if head_position in snake.body[1:]:
            game_over = True
            snake.direction = (0,0)
        
        if not game_over:    
            if delete_tale:
                y, x = snake.move(delete_tale)
                field_[y][x] = 0
            else:
                snake.move(delete_tale)
                apple_position = generate_apple(snake.body, N, M)
                field_[apple_position[0]][apple_position[1]] = 2
                speed -= 10

            y, x = snake.body[0]
            field_[y][x] = 1
        

    field.update(field_, colors)
    main_screen.fill(COLORS['black'])
    field.draw(main_screen)

    pg.display.flip()