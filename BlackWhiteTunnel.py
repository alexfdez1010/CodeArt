import drawBot as draw
from random import random

RESOLUTION: tuple = (8000, 8000)

BLACK: tuple = (0, 0, 0, 1)
WHITE: tuple = (1, 1, 1, 1)


def change_color(color: tuple):
    draw.fill(color[0], color[1], color[2], color[3])


def draw_tunnel(size, margin=100, prob_black_lines=0.1):
    steps = (size // margin) >> 1

    for i in range(steps):

        if random() > 0.5 * (1 - i / steps) + prob_black_lines:

            change_color(WHITE)

        else:

            change_color(BLACK)

        draw.rect(i * margin, i * margin, size - 2 * i * margin, size - 2 * i * margin)


if __name__ == '__main__':
    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw_tunnel(RESOLUTION[0], 1, 0.1)
    draw.saveImage("Tunnel.jpeg")
    draw.endDrawing()
