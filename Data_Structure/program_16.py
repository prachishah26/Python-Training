# Find the elements of the given list which are exactly the same as the entire product of the list except itself
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8

numbers = [1, 5, 1, 10, 50]
def swap(numbers,i,j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp

def sort_array(arr1):
    temp = 0
    while(temp < len(arr1)-1):
        if(arr1[temp]>arr1[temp+1]):
            swap(arr1,temp,temp+1)
            temp = -1 
        temp+= 1
    return arr1

multiplication = 1
number = sort_array(numbers)[-1]
for i in range(0,len(numbers)-1):
    multiplication *= numbers[i]

if multiplication == numbers[-1] :
    print(number)
else:
    print("No such element exists !!")

# ----------------------------------------------------------------------------------------------

