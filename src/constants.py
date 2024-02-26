from pygame.colordict import THECOLORS as COLORS

W_HEIGHT, W_WIDTH = 600, 800
FPS = 10
N, M = 30, 40
C_HEIGHT, C_WIDTH = W_HEIGHT / N, W_WIDTH / M

MURDER_C, ALIVE_C = COLORS["black"], COLORS['white']

colors = {
    0: COLORS['black'],
    1: COLORS["green"],
    2: COLORS["red"]
}