# Return the array which contains the elements which are greater than from its right side
# Sample = [5, 17, 2, 6, 3]


# numbers = [5, 17, 2, 6, 3]
numbers = [10, 5, 7, 12, 3, 6]
nums_greater_than_right = []
for i in range(len(numbers)):
    if i != len(numbers)-1:
        if numbers[i] > max(numbers[i+1:]):
            nums_greater_than_right.append(numbers[i])
    else:
        nums_greater_than_right.append(numbers[i])         
print(nums_greater_than_right)


# ===============================second_method==============================

greater_nums = []
greater_nums.append(numbers[len(numbers)-1])
for i in range(len(numbers)-2,-1,-1):
    if numbers[i] > greater_nums[0]:
        greater_nums.insert(0,numbers[i])

print(greater_nums)


    