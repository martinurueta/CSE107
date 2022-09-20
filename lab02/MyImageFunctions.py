# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

def myImageInverse(inImage):
    rows, cols = inImage.shape
    Copy_inImage = np.zeros(shape=(rows, cols))

    for row in range(0, rows):
        for col in range(0, cols):
            Copy_inImage[row, col] = 255 - inImage[row, col]

    return Copy_inImage
