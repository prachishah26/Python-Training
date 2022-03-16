# Return product of minimum of odd and maximum of even from a given list.

numbers = [2,3,4,5,6,7,8,9,10,11,12,13]

n1 = 0
n2 = 0
max_value = n2
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        if n1 == 0:
            min_value = numbers[index]
            n1 = 1
        if numbers[index] < min_value:
            min_value = numbers[index]
            
    elif numbers[index] % 2 != 0:
        n2 = numbers[index]
        if numbers[index] >= n2:
            max_value = numbers[index]
            
product_of_num = min_value*max_value
print(product_of_num)