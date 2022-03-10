# Write a Python program to add two positive integers without using the '+' operator

a = 14
b = 5
while b!= 0:
    value = a & b
    a = a^b
    b = value << 1
print(a)