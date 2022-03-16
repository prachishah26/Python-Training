# Return product of minimum of odd and maximum of even from a given list.

numbers = [2,3,4,5,6,7,8,9,10,11,12,13]

initial_value1 = 0
initial_value2 = 0
max_value = initial_value2
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        if initial_value1 == 0:
            min_value = numbers[index]
            initial_value1 = 1
        if numbers[index] < min_value:
            min_value = numbers[index]
            
    elif numbers[index] % 2 != 0:
        initial_value2 = numbers[index]
        if numbers[index] >= initial_value2:
            max_value = numbers[index]
            
product_of_num = min_value*max_value
print(product_of_num)