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

# Get access to the pixel values through the matrix.
im_pixels = asarray(im)
rows, cols = im_pixels.shape

# Default value to find max value pixel
max_pixel = 0

# Find max pixel value in for loop
for row in range(0, rows):
    for col in range(0, cols):
        if max_pixel < im_pixels[row, col]:
            max_pixel = im_pixels[row, col]

# Print max pixel value
print("maximum pixel value of org image is :", max_pixel)

#inversed the Image/matrix using myImageInverse function and output matrix
inversed_pixels = myImageInverse(im_pixels)

# Default value to find max value pixel
max_inversed_pixel = 0

# Find max pixel value in for loop
for row in range(0, rows):
    for col in range(0, cols):
        if max_inversed_pixel < inversed_pixels[row, col]:
            max_inversed_pixel = inversed_pixels[row, col]

# Print max pixel value
print("maximum pixel value of inversed image is :", max_inversed_pixel)

# Create image
inversed_im = Image.fromarray(np.uint8(inversed_pixels))

# Show image
inversed_im.show()

# Save Image
inversed_im.save("inversed_Watertower.tif")