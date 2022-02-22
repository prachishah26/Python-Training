# Write a Python program to add two positive integers without using the '+' operator

a =17 
b=21
while b!=0:
    if b>0:
        a+=1
        b-=1
    elif b<0:
        a-=1
        b+=1

print(a)
