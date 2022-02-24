# Find the intersection (common) of two sets and remove those elements from the first set.

a =  {23, 42, 65, 57, 78, 83, 29}
b =  {57, 83, 29, 67, 73, 43, 48}
y = a.intersection(b)
print("same numbers are : ",y)
print("after removing these numbers from first set : ",a-y)
