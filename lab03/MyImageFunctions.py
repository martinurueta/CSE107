import numpy as np
from numpy import asarray
# For sqrt(), floor()
import math

def myImageResize( inImage_pixels, M, N, interpolation_method ):
# This function resize the image based on the pixels and interpolation method for grayscaled images. The methods are nearest and bilinear
#
# Syntax:
#   up_down_sampled_im_bilinear_pixels = myImageResize(upsampled_im_bilinear_pixels, 400, 400, 'bilinear')

#
# Input:
#   inImage_pixels = the image with pixel values that range from 0-255
#   M = The Row of the image to resize
#   N = The Col of the image to resize
#   interpolation_method = the method to do the resize
#
# Output:
#   up_down_sampled_im_bilinear_pixels = the resized image that was created with a method 
# 
# History:
#   M. Urueta   10/22/22     Created    
    data = np.zeros(shape = (M, N))
    row, col = inImage_pixels.shape
    for m in range (1,M+1):
        for n in range (1, N+1):
            x = ((row/M)*(m - 0.5)) + 0.5
            y = ((col/N)*(n - 0.5)) + 0.5
            if interpolation_method == 'nearest' :
                rx = round(x)
                ry = round(y)
                data[m-1,n-1] = inImage_pixels[rx-1, ry-1]
            elif interpolation_method == 'bilinear':
                if (x == int(x)):
                    m1 = x - 1
                    m2 = x - 1
                else:
                    if x < 1:
                        m1, m2 = 1, 2
                    elif x > row - 1:
                        m1, m2  = row - 2, row - 1
                    else:
                        m1 = math.floor(x - 1)
                        m2 = math.ceil(x - 1)
                # y -> n1, n2  which are the nearest col index
                if(y == int(y)):
                    n1 = y - 1
                    n2 = y - 1
                else:
                    if y < 1:
                        n1, n2 = 1, 2
                    elif y > col - 1:
                        n1, n2 = col - 2, col - 1
                    else:
                        n1 = math.floor(y - 1)
                        n2 = math.ceil(y - 1)

                p1 = inImage_pixels[m1, n1]
                p2 = inImage_pixels[m1, n2]
                p3 = inImage_pixels[m2, n1]
                p4 = inImage_pixels[m2, n2]
                p5 = 0
                
                p5 = mybilinear(m1,n1,p1,m1,n2,p2,m2,n1,p3,m2,n2,p4,x - 1,y - 1,p5)
                data[m - 1, n - 1] = p5
    return data

def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5,p5):
# This function preforms the bilinear interpolation to get the pixel value for the interpolated pixel
#
# Syntax:
#   p5 = mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5,p5)
#
# Input:
#   x = the location in x
#   y = the location in y
#   p = the intesity value
#  
#
# Output:
#   p5 = the intesity value 
# 
# History:
#   M. Urueta   10/22/22     Created  
    p5_prime = (p3 - p1) * ((x5 - x1) / (x3 -x1)) + p1
    p5_doubleprime = (p4 - p2) * ((x5 - x2) / (y2 -y1)) + p2
    p5 = (p5_doubleprime - p5_prime) * ((y5 - y1) / (y2 - y1)) + p5_prime
    return p5

def myRMSE(first_im_pixels, sec_im_pixels):
# This function is the root mean squared error. compare the matrix of two image 
#
# Syntax:
#   up_down_bilinear_RMSE = myRMSE( first_im_pixels, sec_im_pixels)
#
# Input:
#   first_im_pixels = the original image matrix
#   sec_im_pixels = the reconstruct image matrix
#  
#
# Output:
#   up_down_bilinear_RMSE = The root mean squared error
# 
# History:
#   M. Urueta   10/22/22     Created 
    total = 0
    M,N = first_im_pixels.shape
    for m in range(0,M):
        for n in range(0,N):
            total += (first_im_pixels[m,n] - sec_im_pixels[m,n]) ** 2
    total = total / (M * N)

    return math.sqrt(total)