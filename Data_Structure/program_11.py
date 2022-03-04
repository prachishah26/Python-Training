# Return product of minimum of odd and maximum of even from a given list.

numbers = [2,3,4,5,6,7,8,9,10,11,12,13]

n1 = 0
n2 = 0
max_value = n2
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        if n1 == 0:
            min_value = numbers[i]
            n1 = 1
        if numbers[i] < min_value:
            min_value = numbers[i]
            
    elif numbers[i] % 2 != 0:
        n2 = numbers[i]
        if numbers[i] >= n2:
            max_value = numbers[i]
            
product_of_num = min_value*max_value
print(product_of_num)