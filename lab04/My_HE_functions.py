# MyHEFunctions.py

# Import numpy
import numpy as np

def compute_histogram( image_pixels ):
    # compute_histogram  Computes the normalized histogram of a grayscale image.
    #
    # Syntax:
    #   hist = compute_histogram( image_pixels )
    #
    # Input:
    #   image_pixels = The image pixels.
    #
    # Output:
    #   hist = The length 256 histogram vector.
    #
    # History:
    #   M. Urueta     11/06/2022   created

    row, col = image_pixels.shape
    h = np.zeros(shape = (256))
    for r in range (0,row):
        for c in range (0, col):
            k = round(image_pixels[r,c],1)
            h[int(k)] = h[int(k)] + 1
    m = 0
    for k in range (0,256):
        m = m + h[k]
    h = h / m
    return h


def equalize( in_image_pixels ): 
    # equalize  Performs histogram equalization on a grayscale image.
    #
    # Syntax:
    #   out_image_pixels = equalize( in_image_pixels )
    #
    # Input:
    #   in_image_pixels = The input image pixels.
    #
    # Output:
    #   out_image_pixels = The output image pixels.
    #
    # History:
    #   M. Urueta     11/06/2022   created
    row, col = in_image_pixels.shape
    out_image_pixels = np.zeros(shape = (row, col))
    h = compute_histogram(in_image_pixels)
    h = np.cumsum(h)
    for r in range (0,row):
        for c in range (0, col):
            k = round(in_image_pixels[r,c],1)
            out_image_pixels[r,c] = round(255*h[int(k)])
    return out_image_pixels

    


def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/23/2022   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()