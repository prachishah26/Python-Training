# Find the max sum of sub array


# import math
numbers = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
numbers = [-1,-2,-3,1,2]
total_max_sum = -1000000
temp_sum = 0

for itr in range(0, len(numbers)):
    temp_sum += numbers[itr]
    # print(temp_sum)
    if(temp_sum > total_max_sum):
        total_max_sum = temp_sum
    if(temp_sum < 0):
        temp_sum = 0       
print(total_max_sum)


