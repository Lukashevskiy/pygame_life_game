import random
import time

def create_field(n, m):
    field = []
    i = 0
    while i < n+2:
        line = []
        j = 0
        while j < m+2:
            line.append(0)
            j += 1

        i += 1
        field.append(line)
    return field

def show_field(field):
    print("-"*2*len(field))
    for line in field:
        for el in line:
            print(el, end=' ')
        print()
    print("-"*2*len(field))


def randomize_field(field):
    n, m = len(field), len(field[0])
    for i in range(1, n):
        for j in range(1, m):
            field[i][j] = random.choice([0, 1])
    return field

def get_count_alive_neighbors(field, i, j):
    neighbors = [
        [-1, -1], 
        [-1, 0], 
        [-1, 1], 
        [0, -1], 
        [0, 1], 
        [1, -1], 
        [1, 0], 
        [1, 1]]

    count = 0
    for neighbor in neighbors:
        y, x = i + neighbor[0], j + neighbor[1]
        if field[y][x] == 1:
            count += 1

    return count
  
def is_alive(field, i, j):
    """
        2 - состояние клетки остается прежним
        3 - состояние клетки = жизнь
        остальное - состояние клетки = смерть
    """
    count_alive_neighbors = get_count_alive_neighbors(field, i, j)

    if count_alive_neighbors == 2:
        return field[i][j]

    if count_alive_neighbors == 3:
        return 1
    
    return 0

def new_field_of_life(field):
    n, m = len(field), len(field[0])
    new_field = create_field(n, m)

    for i in range(1, n):
        for j in range(1, m):
            new_field[i][j] = is_alive(field, i, j)
    
    return new_field