# Write first_number Python program to add two positive integers without using the '+' operator

first_number = 14
second_number = 5
while second_number!= 0:
    value = first_number & second_number
    first_number = first_number^second_number
    second_number = value << 1
print(first_number)