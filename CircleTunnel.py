import drawBot as draw
from random import random

RESOLUTION: tuple = (16000, 16000)

BLACK: tuple = (0, 0, 0, 1)
WHITE: tuple = (1, 1, 1, 1)
RED: tuple = (1, 0 , 0, 1)

def change_color(color : tuple):
    draw.fill(color[0], color[1], color[2], color[3])

def draw_circle_tunnel(size, margin, prob_black_lines):
    steps = (size // margin) >> 1
    step = 1 / (2*steps)

    change_color(BLACK)
    draw.rect(0,0,RESOLUTION[0],RESOLUTION[1])

    for i in range(steps):

        if random() > 0.5 * (1 - i / steps) + prob_black_lines:

            change_color(RED)

        else:

            change_color(BLACK)

        draw.oval(i * margin, i * margin, size - 2 * i * margin, size - 2 * i * margin)

if __name__ == '__main__':

    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw_circle_tunnel(RESOLUTION[0],5,0.1)
    draw.saveImage("CircleTunnel.jpeg")
    draw.endDrawing()