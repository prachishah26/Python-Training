# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

numbers = list(map(int, input("Enter multiple values\n").split(',')))
unique_num = set(numbers)
if len(numbers) == len(unique_num):
    print("yes")
else :
    print("no")
    