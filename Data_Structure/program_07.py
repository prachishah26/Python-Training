# Convert any lower case string to upper case without in-built python functions.

alphabets = "abcdef ghi"
alpha = []

for index in range(len(alphabets)):
    if alphabets[index] == " ":
        alpha.append(" ")
    else:
        alpha.append(alphabets[index])
        alpha[index] = chr((ord(alphabets[index]))-32)

capatalized_alpha = "".join(alpha)
print(capatalized_alpha)