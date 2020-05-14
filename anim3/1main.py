#!/usr/bin/python3.7

from PIL import Image
import numpy as np
import cmath
from numba import jit
from utilities import timer

width = 800
height = 600


x_min = -2.5 #complex(-2.5, -1.5)
x_max =  2.5 #complex(2.5, 1.5)
y_min = -1.5
y_max =  1.5


x_r = x_max - x_min
y_r = y_max - y_min

@jit(nopython=True)
def seq(z_x, z_y, p_x, p_y): return (z_x**2 - z_y**2 + p_x, 2 * z_x * z_y + p_y)

@jit(nopython=True)
def run(iterations):
    x_values = np.zeros((height, width), dtype=np.float32)
    y_values = np.zeros((height, width), dtype=np.float32)
    im_array = np.zeros((height, width), dtype=np.uint8)
    for i in range(iterations):
        print(i)
        for y in range(height):
            for x in range(width):
                _x = x_min + x_r * x/width
                _y = y_min + y_r * y/height
                new_x, new_y = seq(x_values[y][x], y_values[y][x], _x, _y)
                x_values[y][x] = new_x
                y_values[y][x] = new_y
                if (new_x**2 + new_y**2) >= 2: 
                    im_array[y][x] = np.floor(255 * i/iterations)

    return im_array

@timer
def test():
    im_array = run(100)
    return im_array

im = Image.fromarray(test(), mode="L")
im.show()
