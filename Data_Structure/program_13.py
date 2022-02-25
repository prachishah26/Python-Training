# Return the array which contains the elements which are greater than from its right side
# Sample = [5, 17, 2, 6, 3]


numbers = [5, 17, 2, 6, 3]
nums_greater_than_right = []
for i in range(len(numbers)):
    if i != len(numbers)-1:
        if numbers[i] > numbers[i+1]:
            nums_greater_than_right.append(numbers[i])
    else:
        nums_greater_than_right.append(numbers[i])         
print(nums_greater_than_right)