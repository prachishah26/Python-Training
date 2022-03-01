# Find the majority element of the given list.
# Majority element: count of the elements > N/2
# N = length of list

A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
dictionary = {}
for i in range(len(A)):
    dictionary[A[i]] = A.count(A[i])
max_value = max(dictionary.values())
if max_value > len(A)/2:
    print(list(dictionary.keys())[list(dictionary.values()).index(max_value)])
