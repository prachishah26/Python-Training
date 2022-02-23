# Slice list into 3 equal chunks and reverse each chunk

array1 =  [11, 45, 8, 23, 14, 12, 78, 45, 89]
new_arr = []
n = 3
chunks = int((len(array1)/n))
print(chunks)
for i in range(chunks+1):
    a = array1[0:3]
    a.reverse()
    new_arr.append(a)
    array1 = array1[3:]
    if len(array1)==0:
        break

print(new_arr)