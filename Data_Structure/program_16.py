# Find the elements of the given list which are exactly the same as the entire product of the list except itself
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8

numbers = [1, 5, 1, 10, 50]
def swap(numbers,index,j):
    numbers[index],numbers[j] = numbers[j],numbers[index]

def sort_array(list_of_numbers):
    temporary_number = 0
    while(temporary_number < len(list_of_numbers)-1):
        if(list_of_numbers[temporary_number]>list_of_numbers[temporary_number+1]):
            swap(list_of_numbers,temporary_number,temporary_number+1)
            temporary_number = -1 
        temporary_number+= 1
    return list_of_numbers

multiplication = 1
number = sort_array(numbers)[-1]
for index in range(0,len(numbers)-1):
    multiplication *= numbers[index]

if multiplication == numbers[-1] :
    print(number)
else:
    print("No such element exists !!")

# ----------------------------------------------------------------------------------------------

