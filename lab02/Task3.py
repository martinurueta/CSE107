# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

cols = 256
rows = 100
grayscale_pixels = np.zeros(shape=(rows, cols))

for row in range(0, rows):
    for col in range(0, cols):
        grayscale_pixels[row, col] = col

grayscale_im = Image.fromarray(np.uint8(grayscale_pixels))
grayscale_im.show()
grayscale_im.save("grayscale.tif")

Averagepixel = 0

for row in range(0, rows):
    for col in range(0, cols):
        Averagepixel += grayscale_pixels[row, col]

Averagepixel = Averagepixel / (cols * rows)
print ("Average Pixel:", Averagepixel)
