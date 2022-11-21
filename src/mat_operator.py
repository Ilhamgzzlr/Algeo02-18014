import numpy as np

def mat_selisih(list_mat, mat):
    retval = []
    for i in range(0, len(list_mat), 1):
        retval.append(abs(list_mat[i] - mat))
    return (retval)

def mat_covarian(list_mat):
    retval = []
    for i in range(0, len(list_mat), 1):
        retval.append(np.cov(list_mat[i]))
    return (retval)