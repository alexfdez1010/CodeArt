import drawBot as draw
from random import choice, random

RESOLUTION: tuple = (16000, 16000)
BLACK: tuple = (0, 0, 0, 1)

coors = [[0 for _ in range(RESOLUTION[0])] for _ in range(RESOLUTION[1])]
random_coors = []


def put_adj(coor: tuple, size_walk: int):
    global coors

    start_x, start_y = max(coor[0] - size_walk // 2, 0), max(coor[1] - size_walk // 2, 0)
    end_x, end_y = min(coor[0] + size_walk // 2, RESOLUTION[0]-1), min(coor[1] + size_walk // 2, RESOLUTION[1]-1)

    i = start_x

    while i <= end_x:

        j = start_y

        while j <= end_y:
            coors[i][j] = 1
            j += 1

        i += 1


def valid_coor(coor: tuple, size_walk: int) -> bool:
    global coors

    start_x, start_y = coor[0] - size_walk // 2, coor[1] - size_walk // 2
    end_x, end_y = coor[0] + size_walk // 2, coor[1] + size_walk // 2

    i = start_x

    while i <= end_x:

        j = start_y

        while j <= end_y:

            if 0 < i < RESOLUTION[0] and 0 < j < RESOLUTION[1]:

                if coors[i][j] == 1:
                    return False

            else:

                return False

            j += 1

        i += 1

    return True


def draw_square(coor: tuple, size_walk: int):
    start_x, start_y = max(coor[0] - size_walk // 2, 0), max(coor[1] - size_walk // 2, 0)

    draw.rect(start_x, start_y, size_walk, size_walk)


def random_walk(coor: tuple, size_walk: int, limit_walk: int):
    global coors, random_coors

    dif = size_walk // 2

    while limit_walk > 0 and coor is not None:

        put_adj(coor, size_walk)
        draw_square(coor, size_walk)
        random_coors.append(coor)

        ele = []

        new_coor = (coor[0] + size_walk, coor[1])
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        new_coor = (coor[0], coor[1] + size_walk)
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        new_coor = (coor[0], coor[1] - size_walk)
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        new_coor = (coor[0] - size_walk, coor[1])
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        if len(ele) > 0:
            coor = choice(ele)
        else:
            coor = None

        limit_walk -= 1


def draw_random_walk(initial_coor: tuple, size_walk: int, num_walks: int = 10000, limit_walk: int = 1000):
    global coors

    coor = tuple(initial_coor)

    dif = size_walk // 2

    for i in range(num_walks):

        draw.fill(random(), random(), random(), 1)
        if coor is not None:
            random_walk(coor, size_walk, limit_walk)

        print(f"Walk {i + 1}/{num_walks} finished")

        ele = []

        coor = choice(random_coors)

        new_coor = (coor[0] + size_walk, coor[1])
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        new_coor = (coor[0], coor[1] + size_walk)
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        new_coor = (coor[0], coor[1] - size_walk)
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        new_coor = (coor[0] - size_walk, coor[1])
        if valid_coor(new_coor, size_walk): ele.append(new_coor)

        if len(ele) > 0:
            coor = choice(ele)
        else:
            coor = None

    print("\n")


if __name__ == '__main__':
    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw.fill(BLACK[0], BLACK[1], BLACK[2], BLACK[3])
    draw.rect(0, 0, RESOLUTION[0], RESOLUTION[1])
    initial_coor = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)
    draw_random_walk(initial_coor, 41)
    print("Saving the image")
    draw.saveImage("RandomWalks.jpeg")
    print("Finish to save the image")
    draw.endDrawing()
