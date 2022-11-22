import cv2
import numpy as np
import math
import os
from PIL import Image

def euclidean_distance(X, Y):
    return math.sqrt(((Y[0] - X[0]) * (Y[0] - X[0])) + ((Y[1] - X[1]) * (Y[1] - X[1])))

def findBiggest(faces):
    biggest = (0,0,0,0)
    maxArea = 0
    for (x,y,w,h) in faces:
        area = w * h
        if area > maxArea:
            biggest = (x,y,w,h)
            maxArea = area
    return biggest

def deteksi_wajah(img):
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_frontalface_default.xml")
    eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_eye.xml")
    face_coordinate = face_detector.detectMultiScale(img)
    eyes = eye_detector.detectMultiScale(img)

    if (len(eyes) > 1):
        if (len(eyes) > 2):
            ab = abs(eyes[0][1] - eyes[1][1])
            bc = abs(eyes[1][1] - eyes[2][1])
            ac = abs(eyes[0][1] - eyes[2][1])
            if (ab < bc and ab < ac):
                eyes = np.delete(eyes, 2, 0)
            elif (bc < ab and bc < ac):
                eyes = np.delete(eyes, 0, 0)
            else:
                eyes = np.delete(eyes, 1, 0)
        
        eye_1 = eyes[0]
        eye_2 = eyes[1]

        if eye_1[0] < eye_2[0]:
            lEye = eye_1
            rEye = eye_2
        else:
            lEye = eye_2
            rEye = eye_1

        rEye_center = (rEye[0] + int(rEye[2] / 2), rEye[1] + int(rEye[3] / 2))
        lEye_center = (lEye[0] + int(lEye[2] / 2), lEye[1] + int(lEye[3] / 2))
        rEye_x = rEye_center[0]
        rEye_y = rEye_center[1]
        lEye_x = lEye_center[0]
        lEye_y = lEye_center[1]

        if lEye_y > rEye_y:
            proyeksi = (rEye_x, lEye_y)
            dir = -1 #rotate image clockwise
        else:
            proyeksi = (lEye_x, rEye_y)
            dir = 1 #rotate image counterclockwise

        a = euclidean_distance(lEye_center, proyeksi)
        b = euclidean_distance(rEye_center, lEye_center)
        c = euclidean_distance(rEye_center, proyeksi)
        cos = (b*b + c*c - a*a)/(2*b*c)
        sudut = (np.arccos(cos) *180) / np.pi

        if dir == -1:
            sudut = 90 - sudut
        else:
            angle = -(90-sudut)
        img = Image.fromarray(img)
        img = np.array(img.rotate(dir * sudut))

    if len(face_coordinate) > 0:
        face_x, face_y, face_w, face_h = findBiggest(face_coordinate)
        img = img[face_y:face_y + face_h, face_x:face_x + face_w]


    img = cv2.resize(img, (256,256))

    return img


def list_files(directory):
    list_of_files = []
    for folder, direct, file in os.walk(directory):
        for filename in file:
            list_of_files.append(os.path.join(folder, filename))
    return list_of_files

def load_images_folder(folder):
    images = []
    for file in list_files(folder):
        images.append(load_images_file(file))
    return images

def load_images_folder2(folder):
    images = []
    for file in list_files(folder):
        images.append(load_images_file2(file))
    return images

def load_images_file2(image):
    img = cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256))
    return img

def load_images_file(image):
    img = deteksi_wajah(cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256)))
    img = img.ravel()
    img = np.array(img)
    return img

def resize_images(images, size):
    resized_images = []
    for image in images:
        resized_images.append(cv2.resize(image, size))
    return resized_images