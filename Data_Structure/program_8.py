# Return the sum of duplicates elements from the given List
# 			Ex. numbers = [3, 5, 6, 11, 12, 3, 5, 2, 3, 5,3]
# 			Output = 8 (3+5)

numbers = [3, 5, 6, 11, 12, 3, 5, 2]
repeated_value = set()
for i in range(len(numbers)):
    if(numbers.count(numbers[i])>1):
        repeated_value.add(((numbers.count(numbers[i]))-1)*numbers[i])
summation = sum(list(repeated_value))
print(summation)
