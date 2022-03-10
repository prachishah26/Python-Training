# Write a NumPy program to compute the sum of the diagonal elements of a given array.

import numpy as np

square_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
sum_of_diagonals = np.trace(square_matrix)
print(sum_of_diagonals)