import numpy as np
import sympy as sy
from matrix import*


def decom(mat):
    n, m = mat.shape # get the shape of A
    a = np.empty((n, n)) # create an empty matrix for Q
    b = np.empty((n, n)) # create an empty matrix for u
    a[:, 0] = b[:, 0] / np.linalg.norm(b[:, 0])
    b[:, 0] = mat[:, 0]
    R = np.zeros((n, m))

    for i in range(1, n):
        b[:, i] = mat[:, i]
        for j in range(i):
            b[:, i] -= (np.dot(mat[:, i], a[:, j])) * a[:, j] # get each b vector

        a[:, i] = b[:, i] / np.linalg.norm(b[:, i]) # compute each e vetor

    for i in range(n):
        for j in range(i, m):
            R[i, j] = np.dot(mat[:, j], a[:, i]) # compute R matrix

    return a, R


def nilai_eigen(mat):
    pQ = np.eye(mat.shape[0])
    X = np.copy(mat)
    for i in range(1):
        Q, R = decom(X)
        pQ = np.dot(pQ, Q)
        X = np.dot(R, Q)
    return np.diag(X)

def vektor_eigen(mat):
    pQ = np.eye(mat.shape[0])
    X = np.copy(mat)
    for i in range(1):
        Q, R = decom(X)
        pQ = np.dot(pQ, Q)
        X = np.dot(R, Q)
    return pQ





