#!/usr/bin/python3.7

from PIL import Image
import numpy as np
import cmath
from numba import jit
from utilities import timer

width = 1280
height = 720
iterations = 20000
save = True


@jit(nopython=True)
def seq(z, p): return z*z + p

@jit(nopython=True)
def run(iterations, z_min, z_max, z_r):
    im_array = np.zeros((height, width, 3), dtype=np.uint8)
    values = np.zeros((height, width), dtype=np.cfloat)
    discarded = np.full((height, width), False)
    for i in range(iterations):
        #print(i)
        for y in range(height):
            for x in range(width):
                z = z_min + complex(z_r.real * x/width, z_r.imag * y/height)
                #print(z)
                if not discarded[y][x]:
                    values[y][x] = seq(values[y][x], z)
                    if abs(values[y][x]) >= 2: 
                        im_array[y][x] = np.array( [np.floor(255*i/iterations), 255, 255] )
                        discarded[y][x] = True

    return im_array



def take_shot(zoom, filename=""):
    z_r = complex(3, 2) * zoom

    z_center = complex(-0.743643887037158704752191506114774, -0.131825904205311970493132056385139)

    #z_center = complex(-1.19, -0.305)
    z_min = z_center - z_r/2
    z_max = z_center + z_r/2

    im_array = run(iterations, z_min, z_max, z_r)

    im = Image.fromarray(im_array, mode="HSV")
    #im.show()
    if filename == '': filename = f"output_{width}_{height}_{iterations}_{zoom}.png"
    im.convert("RGB").save(filename, "PNG")

#for i, z in enumerate(np.linspace(0.5, 0.00001, 25)):
step = 0.825
z = 0.65
#for i in range(200):
#    z = z * step 
#    #print(i)
#    i = str(i).rjust(6, "0")
#    print(i)
#    take_shot(z, "final1_anim/"+i)

take_shot(z*step**160, filename="zoomed_160.png")

