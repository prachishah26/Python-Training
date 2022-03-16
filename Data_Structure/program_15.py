# Calculate the sum of the major and minor diagonals of the given matrix

matrix = [ [2, 0, 7],
      [4, 1, 9],
      [8, 1, -1], 
     ]
major_diagonal_sum = 0
minor_diagonal_sum = 0

length_of_matrix = len(matrix)-1
for index in range(len(matrix)):
    major_diagonal_sum += matrix[index][index]
    minor_diagonal_sum += matrix[index][length_of_matrix]
    length_of_matrix -= 1

print(major_diagonal_sum)
print(minor_diagonal_sum)