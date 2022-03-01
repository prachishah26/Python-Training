# Calculate the sum of the major and minor diagonals of the given matrix

A = [ [2, 0, 7],
      [4, 1, 9],
      [8, 1, -1], 
     ]
major_diagonal_sum = 0
minor_diagonal_sum = 0

n = len(A)-1
for i in range(len(A)):
    major_diagonal_sum += A[i][i]
    minor_diagonal_sum += A[i][n]
    n -= 1

print(major_diagonal_sum)
print(minor_diagonal_sum)