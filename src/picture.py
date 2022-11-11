import cv2
import os
from matrix import *

def list_files(directory):
    list_of_files = []
    for folder, direct, file in os.walk(directory):
        for filename in file:
            list_of_files.append(os.path.join(folder, filename))
    return list_of_files


def load_images(folder):
    images = []
    for image in list_files(folder):
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def resize_images(images, size):
    resized_images = []
    for image in images:
        resized_images.append(cv2.resize(image, size))
    return resized_images