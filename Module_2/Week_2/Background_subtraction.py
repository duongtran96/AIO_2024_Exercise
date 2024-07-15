import numpy as np
from google.colab.patches import cv2_imshow # type: ignore
import cv2


bg1_image = cv2.imread("/content/GreenBackground.png", 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread("/content/Object.png", 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread("/content/NewBackground.jpg", 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


# function compute
def compute_difference(bg_ing, input_img):
    # convert to gray
    bg_ing = cv2.cvtColor(bg_ing, cv2.COLOR_BGR2GRAY)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

    # subtraction 2 image
    diff = cv2.absdiff(input_img, bg_ing)
    return diff


def compute_binary_mask(difference_single_channel):
    # pixel below 10 change to black, pixel above 10 change to 255 (white)
    _, mask = cv2.threshold(
        difference_single_channel, 11, 255, cv2.THRESH_BINARY)
    return mask


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)

    binary_mask = compute_binary_mask(difference_single_channel)

    binary_mask = np.expand_dims(binary_mask, axis=-1)
    output = np.where(binary_mask == 255, ob_image,  bg2_image)
    return output


out = replace_background(bg1_image, bg2_image, ob_image)
cv2_imshow(out)
