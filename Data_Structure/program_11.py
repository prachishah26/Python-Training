# Return product of minimum of odd and maximum of even from a given list.

numbers = [7, 5,  2, 3, 12, 9, 15, 24]
even_num = []
odd_num = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_num.append(numbers[i])
    else :
        odd_num.append(numbers[i])
product_of_num = min(odd_num)*max(even_num)
print(product_of_num)

