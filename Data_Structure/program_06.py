# Create a function to reverse the entire list without any function and also do not use any indexing or slicing shortcut. Time Complexity O(logn)

numbers = [1,2,3,4,5,21,65]
length_of_number = len(numbers)
def reverse_numbers(numbers):
    for index in range(len(numbers)):
            if index < (length_of_number/2):
                numbers[index], numbers[length_of_number-index-1] = numbers[length_of_number-index-1], numbers[index]
                
    return numbers
print(reverse_numbers(numbers))