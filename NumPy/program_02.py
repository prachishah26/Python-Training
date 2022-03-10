# 2. Write a NumPy program to compute the outer product of two given vectors.
import numpy as np
vector_1 = [1,2,3,4]
vector_2 = [1,2,3,4]

outer_product = np.outer(vector_1,vector_2)
print(outer_product)