import os
from pict import *
from mat_operator import *
from eigen import *
from PIL import Image
import numpy as np


S = np.array(load_images_folder(".\dataset"))
mean = np.mean(S, axis=0) # Calculate mean of images
sel = np.array(abs(S - mean))# Calculate difference between images and mean
trans = np.transpose(sel)
cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
vektoreigen = np.array(vektor_eigen(cov)) # Calculate eigen vector of covariance
vektoreigen = np.dot(vektoreigen, sel)
eigenfaces = np.array(np.dot(sel, vektoreigen)) # Calculate eigen face
# TEST(Inputan)
tes = '.\dataset\Alexandra Daddario.jpg'
TestFace = np.array(load_images_file(tes))
selisihface = np.array(abs(TestFace - mean))
print(S)