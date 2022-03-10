# 1. Write a NumPy program to compute the multiplication of two given matrices.

import numpy as np
first_matrix = np.array([[1,2,3],[4,5,6],[1,1,1]])
second_matrix = np.array([[1,1,1],[2,2,2],[3,3,3]])

# first_matrix = np.array([[1,2],[3,4]])
# second_matrix = np.array([[1,2],[3,4]])

multiplication = first_matrix@second_matrix
print(multiplication)
