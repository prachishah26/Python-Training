# 6. Write a NumPy program to compute the inverse of a given matrix.

import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[1,1,0]])

if np.linalg.det(matrix) == 0:
    print("The given matrix is singular !!! So we can't find inverse of the matrix.")
else:
    inversed = np.linalg.inv(matrix)
    print(inversed)
