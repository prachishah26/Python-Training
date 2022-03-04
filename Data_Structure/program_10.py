# Find the max sum of sub array


import math
numbers = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]

total_max_sum = 0
temp_sum = 0

for itr in range(0, len(numbers)):
    temp_sum += numbers[itr]
    # print(temp_sum)
    if(temp_sum > total_max_sum):
        total_max_sum = temp_sum
        if(temp_sum < 0):
            temp_sum = 0       
print(total_max_sum)


# -------------------------------------------------------------------------------------

# summation = []
# for itr in range(len(numbers)):
#     for j in range(len(numbers)):
#         if itr!= j and itr<j:
#             summation.append((sum(numbers[itr:j+1])))
           
# print(max(summation))
