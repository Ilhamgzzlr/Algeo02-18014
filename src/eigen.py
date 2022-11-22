import numpy as np
import sympy as sy
from matrix import*

def QR(mat):
    n, m = mat.shape # get the shape of A

    Q = np.empty((n, n)) # initialize matrix Q
    u = np.empty((n, n)) # initialize matrix u

    u[:, 0] = mat[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    for i in range(1, n):
        u[:, i] = mat[:, i]
        for j in range(i):
            u[:, i] -= (mat[:, i] @ Q[:, j]) * Q[:, j] # get each u vector

        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i]) # compute each e vetor

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = mat[:, j] @ Q[:, i]

    return Q, R



def eigen_Val(mat):
    pQ = np.eye(mat.shape[0])
    X = np.copy(mat)
    for i in range(1000):
        Q, R = QR(X)
        pQ = pQ @ Q
        X = R @ Q
    return np.diag(X)

def eigen_Vec(mat):
    pQ = np.eye(mat.shape[0])
    X = np.copy(mat)
    for i in range(1000):
        Q, R = QR(X)
        pQ = pQ @ Q
        X = R @ Q
    return pQ





