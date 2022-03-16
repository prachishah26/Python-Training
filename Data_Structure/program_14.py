# Add 1 to given list elements. Do not use string conversion.

numbers = [1,2,3]
length_of_numbers = len(numbers)
flag = -1
for index in range(len(numbers)-1,-1,-1):
    if index == length_of_numbers-1:
        if (numbers[index]+1 < 9):
            numbers[index] += 1
            flag = 0
            break
        elif (numbers[index]+1 > 9):
            numbers[index] = 0
            flag = 1
    
    else:
        if flag == 1:
            if (numbers[index]+1 < 9):
                numbers[index] += 1
                flag = 0
                break
            elif (numbers[index]+1 > 9):
                numbers[index] = 0
                flag = 1
                if index == 0:
                    numbers.insert(0,1)
        
print(numbers)

