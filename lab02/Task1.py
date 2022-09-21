# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Read the image
im = Image.open('Beginnings.jpg')

# Show the image.
im.show()

# Convert image to gray scale.
im_gray = ImageOps.grayscale(im)

#Show gray image
im_gray.show()

#Save gray image
im_gray.save("Beginnings_grayscale.jpg")

# Get access to the pixel values through the matrix im_gray_pixels.
im_gray_pixels = asarray(im_gray)
rows, cols = im_gray_pixels.shape

# Determine the dimensions of the image.
print("Image size is: ", rows, "rows x", cols, "columns")

# Default value to find max value pixel
maxpixel = 0

# Find max pixel value in for loop
for row in range(0, rows):
    for col in range(0, cols):
        if maxpixel < im_gray_pixels[row, col]:
            maxpixel = im_gray_pixels[row, col]

# Print max pixel value
print("maximum pixel value is :", maxpixel)

# Change the rows and cols of the new matrix
ninetydegrees_rows = cols 
ninetydegrees_cols = rows
ninetydegrees_ccw_pixels = np.zeros(shape=(ninetydegrees_rows, ninetydegrees_cols))

# Copy values of from old image but change the rows and cols to ccw rotate image
for row in range(0, ninetydegrees_rows):
    for col in range(0, ninetydegrees_cols):
        ninetydegrees_ccw_pixels[row, col] = im_gray_pixels[col, row]

# Create image
ninetydegrees_ccw_im_gray = Image.fromarray(np.uint8(ninetydegrees_ccw_pixels))

# Show image
ninetydegrees_ccw_im_gray.show()

# Save Image
ninetydegrees_ccw_im_gray.save("Beginnings_grayscale_counterclockwise.jpg")

# create new matrix
ninetydegrees_cw_pixels = np.zeros(shape=(ninetydegrees_rows, ninetydegrees_cols))

# Copy values of from old image but change the rows and cols to cw rotate image
for row in range(0, ninetydegrees_rows):
    for col in range(0, ninetydegrees_cols):
        ninetydegrees_cw_pixels[row, col] = im_gray_pixels[(ninetydegrees_cols-col-1), (ninetydegrees_rows-row-1)]

# Create image
ninetydegrees_cw_im_gray = Image.fromarray(np.uint8(ninetydegrees_cw_pixels))

# Show image
ninetydegrees_cw_im_gray.show()

# Save Image
ninetydegrees_cw_im_gray.save("Beginnings_grayscale_clockwise.jpg")

# Find max pixel in for loop
for row in range(0, ninetydegrees_rows):
    for col in range(0, ninetydegrees_cols):
        if maxpixel < ninetydegrees_cw_pixels[row, col]:
            maxpixel = ninetydegrees_cw_pixels[row, col]
            
# Print max pixel value
print("maximum pixel value is :", maxpixel)