# TASK 1:
# ETA 40 mins - 11.41 AM
# Now, let's imagine a rectangle of height 1 and length 2. The four corner points of the rectangle are:
# a = (0, 0)
# b = (2, 0)
# c = (2, 1)
# d = (0, 1)
# Now, apply the shearing transformation to these four points. Can you imagine the rectangle turning into a parallelogram.
# Shear matrix = [[1, 1], [0, 1]]
# Now the origin has been shifted to (1, 3)
# What will be the output points: - Solve using 2 approaches
# Without using numpy or 2D list
# Use numpy for matrix computation


from re import X
import numpy as np

matrix_ = np.array([[0, 0], [2, 0], [2, 1], [0, 1]])
shear_matrix = np.array([[1, 1], [0, 1]])

new_matrix = shear_matrix @ matrix_.T
print("------------------------------------\n",new_matrix.T)

# after changing the origin---------
print("\nShifted coordinates\n")
# metrices = [new_matrix1,new_matrix2,new_matrix3,new_matrix4 ]
for matrix in new_matrix.T:
    new_coordinates = matrix + np.array([1,3])
    print(new_coordinates)

# without numpy-------------------------------------------------------------------------------

s1 = [1, 1]
s2 = [0, 1]
coordinates = set()
x_axis = [0,2,2,0]
y_axis = [0,0,1,1]
for k, l in zip(x_axis, y_axis):
    a = (s1[0]*k + s1[1]*l)
    b = (s2[0]*k + s2[1]*l)
    coordinates.add((a,b))
print("\nwithout numpy----\n")
print(coordinates)
