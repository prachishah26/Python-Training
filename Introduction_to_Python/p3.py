# Write a Python program to find common divisors between two numbers in a given pair

first_number = int(input("enter first number : "))
second_number = int(input("enter second number : "))

while first_number != second_number :
    if first_number > second_number:
        first_number -= second_number
    else :
        second_number -= first_number

print(first_number)