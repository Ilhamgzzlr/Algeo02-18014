import numpy as np
import sympy as sy
from matrix import*


def Normalize(mat):
    mat = np.square(mat)
    mat = np.sum(mat)
    mat = np.sqrt(mat)
    return mat


def QR(mat):
    n, m = mat.shape                        # n = baris, m = kolom

    x = np.empty((n, n))                    # inisialisasi matriks x
    y = np.empty((n, n))                    # inisialisasi matriks y

    y[:, 0] = mat[:, 0]                     # y0 = a0
    x[:, 0] = y[:, 0] / Normalize(y[:, 0])  # x1 = u1 / ||u1||

    for i in range(1, n):
        y[:, i] = mat[:, i]                 # yi = ai
        for j in range(i):
            y[:, i] -= (mat[:, i] @ x[:, j]) * x[:, j]  # yi = ai - (ai . xj) xj

        x[:, i] = y[:, i] / Normalize(y[:, i])          # xi = yi / ||yi||

    z = np.zeros((n, m))                                # inisialisasi matriks z
    for i in range(n):
        for j in range(i, m):
            z[i, j] = mat[:, j] @ x[:, i]               # compute each e value

    return x, z                                         # return x and z

def eigen_Vec(mat):
    X = np.eye(mat.shape[0])
    Y = np.copy(mat)
    
    for i in range(10):
        W, Z = QR(Y)
        X = X @ W
        Y = Z @ W
        
    return X




