#  Count the occurrence of each element from a list
# Sample: [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

numbers = [11, 45, 8, 11, 23, 45, 23, 45, 89]
numbers_set = set(numbers)
new_numbers = list(numbers_set)
numbers_dict = dict()
for itr in range(len(new_numbers)):
    numbers_dict[new_numbers[itr]] = numbers.count(new_numbers[itr])
print(numbers_dict)


# ===============================without count====================================

numbers = [11, 45, 8, 11, 23, 45, 23, 45, 89]
numbers_set = set(numbers)
numbers_dict = dict()
for itr in numbers:
    if itr not in numbers_dict.keys():
        numbers_dict[itr] = 1
    else:
        j = numbers_dict[itr]
        numbers_dict[itr] = j+1

print(numbers_dict)