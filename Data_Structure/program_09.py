#  Count the subsequence “AG” in the given string.

total_alphabets =  "BCAHGBNAJKGTYUALKWG"
value = 0
for i in range(len(total_alphabets)):
    for j in range(i+1,len(total_alphabets)):
        if total_alphabets[i] == "A" and total_alphabets[j] == "G":
            value += 1

print(value)