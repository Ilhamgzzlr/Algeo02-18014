import numpy as np
import sympy as sy
from matrix import*

lamda = sy.Symbol("x")

M = ([[1,2,3],[1,2,3],[1,2,3]])
i = np.identity(3)
j = konstantaMatrix(i, lamda)
b = kurangMatrix(M, j)
v = kaliMatrix(M, b)

y = kofaktorMatrix(M, 1, 1)
x = determinanMatrix(b)

print(x)




