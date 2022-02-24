#  Count the occurrence of each element from a list
# Sample: [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

numbers = [11, 45, 8, 11, 23, 45, 23, 45, 89]
numbers_set = set(numbers)
new_numbers = list(numbers_set)
numbers_dict = dict()
for i in range(len(new_numbers)):
    numbers_dict[new_numbers[i]] = numbers.count(new_numbers[i])
print(numbers_dict)


# ===============================without count====================================

numbers = [11, 45, 8, 11, 23, 45, 23, 45, 89]
numbers_set = set(numbers)
numbers_dict = dict()
for i in numbers:
    if i not in numbers_dict.keys():
        numbers_dict[i] = 1
    else:
        j = numbers_dict[i]
        numbers_dict[i] = j+1

print(numbers_dict)