# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

def myImageInverse(inImage_pixels):
# This function takes as input of numpy matrix representing a image and outputs another numpy matrix which is the inverse of the input
# For each pixel, output_value = 255 - input_value
#
# Syntax:
#   inversed_pixels = myImageInverse(im_pixels)
#
# Input:
#   im_pixels = the matrix values of the orginal input image
#
# Output:
#   inversed_pixels = the matrix values of the inverse image
# 
# History:
#   M. Urueta   9/19/22     Created

    rows, cols = inImage_pixels.shape
    Copy_inImage_pixels = np.zeros(shape=(rows, cols))

    for row in range(0, rows):
        for col in range(0, cols):
            Copy_inImage_pixels[row, col] = 255 - inImage_pixels[row, col]

    return Copy_inImage_pixels
