from PIL import Image
import cv2
import os
import numpy as np
import math

def images(directory):
    retval = [] ;
    for folder, direct, file in os.walk(directory):
        for name in file:
            retval.append(os.path.join(folder, name))
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

def selisih(a, b):
    return math.sqrt((math.pow(a[0] - b[0], 2)) + (math.pow(a[1] - b[1], 2)))

def deteksi_wajah(wajah):
    haarcascade_eye = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_eye.xml")
    mata = haarcascade_eye.detectMultiScale(wajah)
    haarcascade_frontalface = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_frontalface_default.xml")
    kepala = haarcascade_frontalface.detectMultiScale(wajah)

    if (len(mata) > 1):
        if (len(mata) > 2):
            x = abs(mata[0][1] - mata[1][1])
            y = abs(mata[1][1] - mata[2][1])
            z = abs(mata[0][1] - mata[2][1])
            if (x < y and x < z):
                mata = np.delete(mata, 2, 0)
            elif (y < x and y < z):
                mata = np.delete(mata, 0, 0)
            else:
                mata = np.delete(mata, 1, 0)
        
        mata1 = mata[0]
        mata2 = mata[1]
        if mata1[0] < mata2[0]:
            mata_kiri = mata1
            mata_kanan = mata2
        else:
            mata_kiri = mata2
            mata_kanan = mata1
        pusat_kanan = (mata_kanan[0] + int(mata_kanan[2] / 2), mata_kanan[1] + int(mata_kanan[3] / 2))
        pusat_kiri = (mata_kiri[0] + int(mata_kiri[2] / 2), mata_kiri[1] + int(mata_kiri[3] / 2))
        mata_kanan_x = pusat_kanan[0]
        mata_kanan_y = pusat_kanan[1]
        mata_kiri_x = pusat_kiri[0]
        mata_kiri_y = pusat_kiri[1]

        if mata_kiri_y > mata_kanan_y:
            proyeksi = (mata_kanan_x, mata_kiri_y)
            dirotasi = -1  # right eye on top 
        else:
            proyeksi = (mata_kiri_x, mata_kanan_y)
            dirotasi = 1    # left eye on top
        kiri_proyeksi = selisih(pusat_kiri, proyeksi)
        kanan_kiri = selisih(pusat_kanan, pusat_kiri)
        kanan_proyeksi = selisih(pusat_kanan, proyeksi)
        putar = (kanan_kiri*kanan_kiri + kanan_proyeksi*kanan_proyeksi - kiri_proyeksi*kiri_proyeksi)/(2*kanan_kiri*kanan_proyeksi)
        sudut = (np.arccos(putar) *180) / np.pi

        if dirotasi == -1:
            sudut = 90 - sudut
        else:
            angle = -(90-sudut)    
        wajah = Image.fromarray(wajah)
        wajah = np.array(wajah.rotate(dirotasi * sudut))

    wajah = cv2.resize(wajah, (256,256))

    return wajah