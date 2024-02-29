from .constants import N, M

class Snake:
    def __init__(self, position, direction):
        self.direction = direction
        self.body = [position]

    def move(self, delete_tale):
        y, x = self.body[0]
        dy, dx = self.direction

        y += dy
        x += dx
        
        if y == 0:
            y = N
        if x == 0:
            x = M
        if y == N+1:
            y = 1
        if x == M+1:
            x = 1

        self.body.insert(0, (y, x))
        if delete_tale:
            return self.body.pop()
