# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Create cols and rows of the matix
cols = 256
rows = 100

# Create a 100x256 matrix that has 0 in each value
grayscale_pixels = np.zeros(shape=(rows, cols))

# Change values of each pixel = to that column number they are on
for row in range(0, rows):
    for col in range(0, cols):
        grayscale_pixels[row, col] = col
# Create image from the matrix
grayscale_im = Image.fromarray(np.uint8(grayscale_pixels))

# Show image
grayscale_im.show()

# Save image
grayscale_im.save("grayscale.tif")

# Create a default value for average pixel
Averagepixel = 0

# Add up all the values in the matrix
for row in range(0, rows):
    for col in range(0, cols):
        Averagepixel += grayscale_pixels[row, col]

# find the average value (add up all the values) / (total # of values)
Averagepixel = Averagepixel / (cols * rows)

# Print the average pixel value
print ("Average Pixel:", Averagepixel)
