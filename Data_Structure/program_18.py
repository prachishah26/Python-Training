# Find the majority element of the given list.
# Majority element: count of the elements > N/2
# N = length of list

numbers = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
dictionary = {}
for index in range(len(numbers)):
    dictionary[numbers[index]] = numbers.count(numbers[index])
max_value = max(dictionary.values())
if max_value > len(numbers)/2:
    print(list(dictionary.keys())[list(dictionary.values()).index(max_value)])
