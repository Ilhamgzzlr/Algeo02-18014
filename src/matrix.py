#   Membuat dan Menampilkan Matriks
import numpy as np

def buatMatrix (Rows, Cols):
    mat = [[0 for j in range(Cols)] for i in range(Rows)]
    return (mat)

def displayMatrix (mat):
    row = len(mat)
    col = len(mat[0])
    
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            if (j == col-1):
                print(mat[i][j])
            else:
                print(mat[i][j] , end=' ')
    print("\n")

#   Membuat dan Menampilkan List Matriks
def buatListMatrix (N, Rows, Cols):
    l = [[[0 for j in range(Cols)] for i in range(Rows)] for k in range(N)]
    return (l)

def displayListMatrix (l):
    N = len(l)
    for k in range(0, N, 1):
        displayMatrix(l[k])

#   Operasi Terhadap Matriks
def tambahMatrix (mat1, mat2):
    row = len(mat1)
    col = len(mat1[0])
    ret = buatMatrix(row, col)
    
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           ret[i][j] = mat1[i][j] + mat2[i][j]
    return (ret)

def kurangMatrix (mat1, mat2):
    row = len(mat1)
    col = len(mat1[0])
    ret = buatMatrix(row, col)
    
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           ret[i][j] = mat1[i][j] - mat2[i][j]
    return (ret)

def kaliMatrix (mat1, mat2):
    row = len(mat1)
    col = len(mat2[0])
    ret = buatMatrix(row, col)
    
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            for k in range(0, len(mat1[0]), 1):
                ret[i][j] = ret[i][j] + (mat1[i][k] * mat2[k][j])
    return (ret)

def matrixBagi (mat, k):
    row = len(mat)
    col = len(mat[0])
    ret = buatMatrix(row, col)
    
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           ret[i][j] = mat[i][j]/k
    return (ret)

def transposeMatrix (mat):
    row = len(mat)
    col = len(mat[0])
    ret = buatMatrix(row, col)
    
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           ret[i][j] = mat[j][i]
    return (ret)

def konstantaMatrix (mat, k):
    row = len(mat)
    col = len(mat[0])
    ret = buatMatrix(row, col)
    
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           ret[i][j] = mat[i][j]*k
    return (ret)

def kofaktorMatrix (mat, x, y):
    row = len(mat)
    col = len(mat[0])
    ret = buatMatrix(row-1, col-1)
    
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            if (i != x and j != y):
                if (i < x and j < y):
                    ret[i][j] = mat[i][j]
                elif (i < x and j > y):
                    ret[i][j-1] = mat[i][j]
                elif (i > x and j < y):
                    ret[i-1][j] = mat[i][j]
                else:
                    ret[i-1][j-1] = mat[i][j]
    return (ret)

def determinanMatrix (mat):
    row = len(mat)
    col = len(mat[0])
    ret = 0
    
    if (row == col):
        if (row == 2):
            ret = (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
        else:
            for i in range(0, row, 1):
                ret = ret + (mat[0][i] * determinanMatrix(kofaktorMatrix(mat, 0, i)))
    return (ret)