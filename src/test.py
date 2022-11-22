from eigen import *
import numpy as np
matriks = np.array([[0, 0, -2], [1, 2, 1], [1, 0, 3]])
matriks2 = np.array([[10, 0, 2], [0, 10, 4], [2, 4, 2]])
print(eigen_Val(matriks))
print_Matrix(eigen_Vec(matriks))
print(eigen_Val(matriks2))
print_Matrix(eigen_Vec(matriks2))
