#  Count the occurrence of each element from a list
# Sample: [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

array = [11, 45, 8, 11, 23, 45, 23, 45, 89]
myset = set(array)
new_array = list(myset)
dictionary = dict()
for i in range(len(new_array)):
    dictionary[new_array[i]] = array.count(new_array[i])
print(dictionary)
