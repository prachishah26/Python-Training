# Return the array which contains the elements which are greater than from its right side
# Sample = [5, 17, 2, 6, 3]


# numbers = [5, 17, 2, 6, 3]
numbers = [10, 5, 7, 12, 3, 6]
nums_greater_than_right = []
for index in range(len(numbers)):
    if index != len(numbers)-1:
        if numbers[index] > max(numbers[index+1:]):
            nums_greater_than_right.append(numbers[index])
    else:
        nums_greater_than_right.append(numbers[index])         
print(nums_greater_than_right)


# ===============================second_method==============================

# greater_nums = []
# greater_nums.append(numbers[len(numbers)-1])
# for index in range(len(numbers)-2,-1,-1):
#     if numbers[index] > greater_nums[0]:
#         greater_nums.insert(0,numbers[index])

# print(greater_nums)


    