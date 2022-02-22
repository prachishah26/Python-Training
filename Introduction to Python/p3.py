# Write a Python program to find common divisors between two numbers in a given pair

a = int(input("enter first number : "))
b = int(input("enter second number : "))

while a != b :
    if a > b:
        a -= b
    else :
        b -= a

print(a)