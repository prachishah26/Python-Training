# Write a Python program to filter(even and odd) a list of integers using Lambda.

# ===============================================lambda=================================================

numbers = list(map(int, input("Enter the elements\n").split(',')))

even = []
odd = []
expression = lambda y : y%2
for element in numbers:
    
    # print(expression)
    if expression(element) == 0:
        even.append(element)
    else :
        odd.append(element)
print("even numbers are : " , even)
print("odd numbers are : ",odd)


# =======================================list comprehension ============================================

even1 = [element for element in numbers if element%2 == 0]
odd1 = [element for element in numbers if element%2 != 0]
print("Even numbers are : ", even1)
print("odd numbers are : ",odd1)