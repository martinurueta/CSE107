# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

#import MyImageFunctions.py
from MyImageFunctions import myImageInverse


# Read the image
im = Image.open('Watertower.tif')

# Show the image.
im.show()

# Get access to the pixel values through the matrix im_gray_pixels.
im_pixels = asarray(im)
rows, cols = im_pixels.shape
max_pixel = 0

for row in range(0, rows):
    for col in range(0, cols):
        if max_pixel < im_pixels[row, col]:
            max_pixel = im_pixels[row, col]

print("maximum pixel value of org image is :", max_pixel)

inversed_pixels = myImageInverse(im_pixels)

max_inversed_pixel = 0

for row in range(0, rows):
    for col in range(0, cols):
        if max_inversed_pixel < inversed_pixels[row, col]:
            max_inversed_pixel = inversed_pixels[row, col]

print("maximum pixel value of inversed image is :", max_inversed_pixel)

inversed_im = Image.fromarray(np.uint8(inversed_pixels))

inversed_im.show()
inversed_im.save("inversed_Watertower.tif")




