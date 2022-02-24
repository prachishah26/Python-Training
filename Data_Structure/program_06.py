# Create a function to reverse the entire list without any function and also do not use any indexing or slicing shortcut. Time Complexity O(logn)


numbers = [1,2,3,4,5,21]
n = len(numbers)
def reverse_numbers(numbers):
    for i in range(len(numbers)):
        if n%2 != 0:
            if i < (n/2)-1:
                c = numbers[i]
                numbers[i] = numbers[n-i-1]
                numbers[n-i-1] = c
        else:
            if i < n/2:
                c = numbers[i]
                numbers[i] = numbers[n-i-1]
                numbers[n-i-1] = c
    return numbers
print(reverse_numbers(numbers))