from PIL import Image
import cv2
import os
import numpy as np
import math

def images(directory):
    retval = [] ;
    for folder, direct, file in os.walk(directory):
        for filename in file:
            retval.append(os.path.join(folder, filename))
    return retval

def open_folder(directory):
    retval_images = []
    for file in images(directory):
        retval_images.append(open_image(file))
    return retval_images

def open_image(gambar):
    foto = deteksi_wajah(cv2.resize(cv2.imread(gambar, cv2.IMREAD_GRAYSCALE), (256, 256)))
    foto = foto.ravel()
    foto = np.array(foto)
    return foto

def kompress(gambar, ukuran):
    kompress = []
    for foto in gambar:
        kompress.append(cv2.resize(foto, ukuran))
    return kompress

def selisih(a, b):
    return math.sqrt((math.pow(a[0] - b[0], 2)) + (math.pow(a[1] - b[1], 2)))
    
def banyak_wajah(ukuran):
    max = (0,0,0,0)
    inisial = 0
    
    for (w,x,y,z) in ukuran:
        area = y * z
        if area > inisial:
            max = (w,x,y,z)
            inisial = area
            
    return max

def deteksi_wajah(wajah):
    haarcascade_eye = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_eye.xml")
    mata = haarcascade_eye.detectMultiScale(wajah)
    haarcascade_frontalface = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_frontalface_default.xml")
    kepala = haarcascade_frontalface.detectMultiScale(wajah)

    if (len(mata) > 1):
        if (len(mata) > 2):
            ab = abs(mata[0][1] - mata[1][1])
            bc = abs(mata[1][1] - mata[2][1])
            ac = abs(mata[0][1] - mata[2][1])
            if (ab < bc and ab < ac):
                mata = np.delete(mata, 2, 0)
            elif (bc < ab and bc < ac):
                mata = np.delete(mata, 0, 0)
            else:
                mata = np.delete(mata, 1, 0)
        
        eye_1 = mata[0]
        eye_2 = mata[1]

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
            dir = -1
        else:
            proyeksi = (lEye_x, rEye_y)
            dir = 1 

        a = selisih(lEye_center, proyeksi)
        b = selisih(rEye_center, lEye_center)
        c = selisih(rEye_center, proyeksi)
        cos = (b*b + c*c - a*a)/(2*b*c)
        sudut = (np.arccos(cos) *180) / np.pi

        if dir == -1:
            sudut = 90 - sudut
        else:
            angle = -(90-sudut)
        wajah = Image.fromarray(wajah)
        wajah = np.array(wajah.rotate(dir * sudut))

    if len(kepala) > 0:
        w, x, y, z = banyak_wajah(kepala)
        wajah = wajah[x : x + z, w : w + y]

    wajah = cv2.resize(wajah, (256,256))

    return wajah