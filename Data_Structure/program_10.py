# Find the max sum of sub array


import math
numbers = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
summation = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i!= j and i<j:
            summation.append((sum(numbers[i:j+1])))
           
print(max(summation))
