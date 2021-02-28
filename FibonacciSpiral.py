import drawBot as draw
from random import random

RESOLUTION: tuple = (16000, 16000)
BLACK: tuple = (0, 0, 0, 1)

COEFS: tuple = ((-1, -1), (1, -1), (1, 1), (-1, 1))


def draw_square(p1: tuple, p2: tuple):
    draw.fill(random(), random(), random(), 1)

    corner_1, corner_2 = (p1[0], p2[1]), (p2[0], p1[1])

    draw.polygon(p1, corner_1, p2, corner_2)


def draw_spiral(size: float):
    points = generate_points(size)

    draw.fill(0, 0, 0, 1)
    draw.rect(0, 0, size, size)

    for i in range(len(points) - 1):
        draw_square(points[i], points[i + 1])


def generate_points(size: float) -> tuple:
    points = [(size / 2, size / 2)]
    radios = []
    num1, num2 = 0, 50
    i = 0

    while 0 <= points[i][0] < size or 0 <= points[i][1] < size:
        point = points[i][0] + num2 * COEFS[i % 4][0], points[i][1] + num2 * COEFS[i % 4][1]

        points.append(point)
        radios.append(num2)

        i += 1

        num1, num2 = num2, num1 + num2

    return points


if __name__ == '__main__':
    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw_spiral(RESOLUTION[0])
    draw.saveImage("FibonacciSpiral.jpeg")
    draw.endDrawing()
