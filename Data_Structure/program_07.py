# Convert any lower case string to upper case without in-built python functions.

alphabets = "abcdef ghi"
alpha = []

for i in range(len(alphabets)):
    if alphabets[i] == " ":
        alpha.append(" ")
    else:
        alpha.append(alphabets[i])
        alpha[i] = chr((ord(alphabets[i]))-32)

capatalized_alpha = "".join(alpha)
print(capatalized_alpha)