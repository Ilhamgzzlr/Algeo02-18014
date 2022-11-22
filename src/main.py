import os
from pict import *
from eigen import *
from PIL import Image
import numpy as np


S = np.array(open_folder(".\dataset"))
H = np.transpose(S)
mean = np.mean(S, axis=0) # Calculate mean of images
meanimage = mean.reshape(256, 256)

sel = np.array(abs(S - mean))# Calculate difference between images and mean
trans = np.transpose(sel)
cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
cov = cov/len(cov)

eigenvector = np.array(eigen_Vec(cov)) # Calculate eigen vector of covariance


for i in range(len(eigenvector)):
    norm = Normalize(eigenvector[i])
    eigenvector[i] = eigenvector[i]/norm

eigenfaces = np.array(np.matmul(eigenvector.T, sel)) # Calculate eigen face
weight = np.array(np.matmul(eigenfaces, sel.T))

test = '.\dataset\Tom Cruise.jpg'
TestFace = np.array(open_image(test))
selisihface = np.array(abs(TestFace - mean))
selisihfaces = selisihface.reshape(65536, 1)
weighttest = np.array(np.matmul(eigenfaces, selisihfaces))

a = np.array(np.square(weight - weighttest))
b = np.sum(a, axis=0)
euclidean = np.sqrt(b)

minus = min(euclidean)
def searchIndex (L, minus):
    for i in range (len(L)):
        if (L[i] == minus):
            return i+1

index = searchIndex(euclidean, minus)
print(index)
# print(min(euclidean))
for i in range(len(S)):
    if i == index-1:
        S = S[i].reshape(256, 256)
        image = Image.fromarray(S)
        image.show()




















# Calculate covariance of difference
# vektoreigen = np.array(eigen_Val(cov)) # Calculate eigen vector of covariance
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
#     return/
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
    

# S = np.array(load_images_folder(".\dataset"))
# mean = np.mean(S, axis=0) # Calculate mean of images
# sel = np.array(abs(S - mean))# Calculate difference between images and mean
# trans = np.transpose(sel)
# cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
# vektoreigen = np.array(vektor_eigen(cov)) # Calculate eigen vector of covariance
# vektoreigen = np.dot(vektoreigen, sel)
# eigenfaces = np.array(np.dot(sel, vektoreigen)) # Calculate eigen face
# # TEST(Inputan)
# tes = '.\dataset\Alexandra Daddario.jpg'
# TestFace = np.array(load_images_file(tes))
# selisihface = np.array(abs(TestFace - mean))
# print(S)