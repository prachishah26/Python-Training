#  Count the subsequence “AG” in the given string.

total_alphabets =  "BCAHGBNAJKGTYUALKWG"
count = 0
total_AG = 0
for i in range(len(total_alphabets)):
    if total_alphabets[i]=="A":
        count += 1
    if total_alphabets[i]=="G":
        total_AG += count
print(total_AG)


# -----------------------------------------------------------------------------------------

# value = 0
# for i in range(len(total_alphabets)):
#     for j in range(i+1,len(total_alphabets)):
#         if total_alphabets[i] == "A" and total_alphabets[j] == "G":
#             value += 1

# print(value)