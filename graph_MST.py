import drawBot as draw
from random import randint, random, seed
from math import sqrt
from queue import PriorityQueue

RESOLUTION = (16000, 16000)
POINT_SIZE = 75


def random_lighter():
    return min(max(random() * 2,0.4), 1)


def generate_random_points(n: int) -> list:
    return [(randint(0, RESOLUTION[0]), randint(0, RESOLUTION[1])) for _ in range(n)]


def get_adj_matrix(points: list) -> list:
    n: int = len(points)
    distance = lambda a, b: sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    adj_matrix: list = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            adj_matrix[i][j] = distance(points[i], points[j])

    return adj_matrix


def draw_point(point: tuple) -> None:
    draw.fill(random_lighter(), random_lighter(), random_lighter(), 1)
    draw.strokeWidth(0)
    draw.oval(point[0] - POINT_SIZE / 2, point[1] - POINT_SIZE / 2, POINT_SIZE, POINT_SIZE)


def draw_line(a: tuple, b: tuple) -> None:
    draw.stroke(random_lighter(), random_lighter(), random_lighter(), 1)
    draw.strokeWidth(POINT_SIZE / 10)
    draw.line(a, b)


def draw_prim(points: list) -> None:
    n: int = len(points)
    adj_matrix: list = get_adj_matrix(points)

    edges = PriorityQueue()
    visited: list = [False for _ in range(n)]

    count_visited: int = 1
    vertex: int = randint(0, n - 1)

    visited[vertex] = True

    while count_visited < n:

        for i in range(n):
            if not visited[i]:
                edges.put((adj_matrix[vertex][i], vertex, i))

        edge: tuple = None
        while edge is None:
            edge = edges.get()
            if visited[edge[2]]:
                edge = None

        draw_line(points[edge[1]], points[edge[2]])
        vertex = edge[2]
        visited[vertex] = True
        count_visited += 1

    for point in points:
        draw_point(point)


if __name__ == "__main__":
    seed(0)
    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw.fill(0)
    draw.rect(0, 0, RESOLUTION[0], RESOLUTION[1])
    draw_prim(generate_random_points(1000))
    draw.saveImage("MST.jpeg")
    draw.endDrawing()
