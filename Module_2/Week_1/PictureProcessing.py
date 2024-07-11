# !gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB

# Method Lightness

import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread("/content/dog.jpeg")


def rbg2gray_by_lightness(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    max_val = np.maximum(np.maximum(r, g), b)
    min_val = np.minimum(np.minimum(r, g), b)
    gray = (min_val + max_val) / 2
    print(gray)
    return gray


gray = rbg2gray_by_lightness(img)
print(gray[0, 0])
# 12 Answer A

# method Average


def rbg2gray_by_average(rgb):
    gray = np.mean(rgb, axis=2)
    return gray


gray = rbg2gray_by_average(img)
print(gray[0, 0])
# 13: Answer A

# method Luminosity


def rbg2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.21 * r + 0.72 * g + 0.07 * b
    return gray


gray = rbg2gray(img)
print(gray[0, 0])
# 14: Answer C
