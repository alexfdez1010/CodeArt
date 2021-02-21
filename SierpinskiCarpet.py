import drawBot as draw
from random import random

RESOLUTION = (16000,16000)
BLACK : tuple = (0, 0, 0, 1)

def draw_sierpinski_r(x_1 ,y_1 ,x_2 ,y_2, limit = 6):

    step = (x_2 - x_1) / 3

    draw.fill(random(),random(),random(),1)

    draw.rect(x_1 + step, y_1 + step, step, step)

    if limit > 0:
        
        for i in range(3):

            for j in range(3):
                
                if i != 1 or j != 1:

                    new_x_1 = x_1 + i * step
                    new_y_1 = y_1 + j * step
                    new_x_2 = x_2 - (2 - i) * step
                    new_y_2 = y_2 - (2 - j) * step

                    draw_sierpinski_r(new_x_1, new_y_1, new_x_2, new_y_2, limit - 1)

def draw_sierpinski(size,limit = 10):
    draw_sierpinski_r(0,0,size,size,limit)

if __name__ == '__main__':

    draw.newDrawing()
    draw.size(RESOLUTION[0], RESOLUTION[1])
    draw.fill(BLACK[0],BLACK[1],BLACK[2],BLACK[3])
    draw_sierpinski(RESOLUTION[0],7)
    draw.saveImage("SierpinskiCarpet.jpeg")
    draw.endDrawing()