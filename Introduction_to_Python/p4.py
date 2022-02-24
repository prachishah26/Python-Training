# Write a Python program to filter(even and odd) a list of integers using Lambda.

# ===============================================lambda=================================================

numbers = list(map(int, input("Enter the elements\n").split(',')))

even = []
odd = []
x = lambda y : y%2
for i in numbers:
    
    # print(x)
    if x(i) == 0:
        even.append(i)
    else :
        odd.append(i)
print("even numbers are : " , even)
print("odd numbers are : ",odd)


# =======================================list comprehension ============================================

even1 = [i for i in numbers if i%2 == 0]
odd1 = [i for i in numbers if i%2 != 0]
print("Even numbers are : ", even1)
print("odd numbers are : ",odd1)