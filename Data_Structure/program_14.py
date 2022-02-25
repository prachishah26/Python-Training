# Add 1 to given list elements. Do not use string conversion.

numbers = [3, 2,1]
n = len(numbers)
flag = -1
for i in range(len(numbers)-1,-1,-1):
    if i == n-1:
        if (numbers[i]+1 < 9):
            numbers[i] += 1
            flag = 0
            break
        elif (numbers[i]+1 > 9):
            numbers[i] = 0
            flag = 1
    if i == 0:
        if (numbers[i]+1 > 9):
            numbers[i] = 0
            numbers.insert(0,1)
    else:
        if flag == 1:
            if (numbers[i]+1 < 9):
                numbers[i] += 1
                flag = 0
                break
        elif (numbers[i]+1 > 9):
            numbers[i] = 0
            flag = 1

print(numbers)