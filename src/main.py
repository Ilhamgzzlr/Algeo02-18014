import os
from pict import *
from mat_operator import *
from eigen import *
from PIL import Image
import numpy as np


S = np.array(load_images_folder("./dataset"))

# mean = np.mean(S, axis=0) # Calculate mean of images
# sel = np.array(abs(S - mean))# Calculate difference between images and mean
# trans = np.transpose(sel)
# cov = np.array(np.dot(sel, trans))# Calculate covariance of difference
# vektoreigen = np.array(eigVec(cov)) # Calculate eigen vector of covariance
# eigenfaces = np.array(np.dot(trans, vektoreigen)) # Calculate eigen face
# # TEST(Inputan)
# tes = '.\dataset\Alexandra Daddario.jpg'
# TestFace = np.array(load_images_file(tes))
# selisihface = np.array(abs(TestFace - mean))
# kamunanya = np.array(np.dot(selisihface, eigenfaces))
# eigenfacestes = np.array(np.dot(eigenfaces, kamunanya))
# print(eigenfacestes)
# def jarak(x,y):
#     dist = 0
#     for i in range(len (x)):
#         dist += math.pow((x[i]-y[i]),2)
#     return dist

# print(jarak(eigenfaces, eigenfacestes))
# print(S.shape)
# print(mean.shape)
# print(eigenfaces.shape)
# print(TestFace.shape)

# print(selisi hface.shape)
# print(eigenfacestes.shape)
# print(jarak(eigenfaces,eigenfacestes))
# print(jarak.shape)


# EUCLIDIAN DISTANCE
# euclidean = []
# minus = 0
# for i in range (len(eigenfaces)):
#     euclidean = np.linalg.norm(np.transpose(eigenfaces[i]) - eigenfacestes)
#     if (i == 0) :
#         minus = euclidean
#         capex = i
#     else :
#         if (minus > euclidean) :
#             minus = euclidean
#             capex = i
# print(capex)
# print(euclidean)


S = np.array(load_images_folder(".\dataset"))
mean = np.mean(S, axis=0)  # Calculate mean of images
sel = np.array(abs(S - mean))  # Calculate difference between images and mean
trans = np.transpose(sel)
cov = np.array(np.matmul(sel, trans))  # Calculate covariance of difference
vektoreigen = np.array(eigen_Vec(cov))  # Calculate eigen vector of covariance
vektoreigen = np.dot(vektoreigen, sel)
eigenfaces = np.array(np.dot(sel, vektoreigen))  # Calculate eigen face
# TEST(Inputan)
tes = '.\dataset\Alexandra Daddario.jpg'
TestFace = np.array(load_images_file(tes))
selisihface = np.array(abs(TestFace - mean))
print(S)
# Euclidean Distance
database = load_images_folder(".\dataset")
minimumdiff = eigen_Val(database[0]) - eigen_Val(TestFace)
minimumindex = 0
for i in range(len(database)):
    currentdiff = eigen_Val(database[i]) - eigen_Val(TestFace)
    if currentdiff <= minimumdiff:
        minimumdiff = currentdiff
        minimumindex = i
print(database[minimumindex])
