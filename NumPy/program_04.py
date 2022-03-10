#  Write a NumPy program to compute the determinant of a given square array.

import numpy as np

square_matrix = np.array([[1,2,3],[4,5,6],[1,1,0]])
determinant = np.linalg.det(square_matrix) 
print(determinant)