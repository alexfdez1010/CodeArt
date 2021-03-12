import drawBot as draw
from random import random
from math import sqrt

RESOLUTION = (16000, 16000)
BLACK: tuple = (0, 0, 0, 1)

def draw_sierpinski_r(x_1, y_1, x_2, y_2, x_3, y_3, limit=6):
    draw.fill(random(),random(),random(),1)

    draw.polygon((x_1, y_1), (x_2, y_2), (x_3, y_3))

    side = (x_2 - x_1) / 2
    desp = sqrt(3 / 4) * side

    if limit > 0:
        draw_sierpinski_r(x_1 - side / 2, y_1 - desp, x_1 + side / 2, y_1 - desp, x_1, y_3, limit - 1)
        draw_sierpinski_r(x_1 + side / 2, y_1 + desp, x_2 - side / 2, y_2 + desp, x_1 + side, y_1, limit - 1)
        draw_sierpinski_r(x_3 + side / 2, y_3 + desp, x_2 + side / 2, y_2 - desp, x_3 + side, y_3, limit - 1)


def draw_sierpinski(side, limit=10):
    c_x, c_y = RESOLUTION[0] / 2, RESOLUTION[1] / 2
    adj = RESOLUTION[1] / 7.5
    desp = sqrt(3 / 4) * side
    draw.fill(BLACK[0], BLACK[1], BLACK[2], BLACK[3])
    draw.rect(0, 0, RESOLUTION[0], RESOLUTION[1])
    draw_sierpinski_r(c_x - side / 2, c_y + desp / 2 - adj, c_x + side / 2, c_y + desp / 2 - adj, c_x,
                      c_y - desp / 2 - adj, limit)


if __name__ == '__main__':
    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw_sierpinski(RESOLUTION[0] / 2.2, 8)
    draw.saveImage("SierpinskiTriangle.jpeg")
    draw.endDrawing()
