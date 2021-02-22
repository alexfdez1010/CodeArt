import drawBot as draw

RESOLUTION : tuple = (16000, 16000)
BLACK : tuple = (0, 0, 0, 1)

COEF : tuple = ((-1, -1), (1, -1), (1, 1), (-1, 1))


def draw_spiral(size):
    points = [(size / 2, size / 2)]
    num1, num2 = 0, 1
    i = 0

    path = draw.BezierPath()
    path.moveTo(points[0])
    draw.fill(None)
    draw.stroke(0)
    draw.strokeWidth(25)

    arc_point = [0,0]

    while 0 <= points[i][0] < size and 0 <= points[i][1] < size:
        point = points[i][0] + num2 * COEF[i % 4][0], points[i][1] + num2 * COEF[i % 4][1]
        points.append(point)

        i += 1

        arc_point[0] = points[i - 1][0] if i & 1 else points[i][0]
        arc_point[1] = points[i][1] if i & 1 else points[i - 1][1]
        draw.stroke(0)
        draw.fill(None)

        path.moveTo(points[i - 1])
        path.arcTo(points[i], arc_point, num2)

        num1, num2 = num2, num1 + num2

    draw.drawPath(path)
    path.endPath()


if __name__ == '__main__':
    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw_spiral(RESOLUTION[0])
    draw.saveImage("FibonacciSpiral.jpeg")
    draw.endDrawing()
