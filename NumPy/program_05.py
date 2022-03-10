#  Write a NumPy program to compute the eigenvalues and eigenvectors of a given square array.

import numpy as np

square_matrix = np.array([[1, 2],
                        [2, 3]])

eigen_values, eigen_vectors = np.linalg.eig(square_matrix)

print("Eigen values are : ", eigen_values)
print("Eigen vectors are : ", eigen_vectors)