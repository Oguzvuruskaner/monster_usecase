import cv2
import numpy as np


def get_whitened_image(img):


    ee = int("ee",base=16)
    ff = int("ff",base=16)

    np.all(img[:, :] == (ff, ff, ff), axis=2)

    background_pixels = np.logical_or(np.all(img[:, :] == (ff, ff, ff), axis=2),np.all(img[:, :] == (ee, ee, ee), axis=2))

    img = cv2.cvtColor(img,cv2.COLOR_RGB2RGBA)
    img[background_pixels,3] = 0
    return img