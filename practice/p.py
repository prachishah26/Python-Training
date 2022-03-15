number = 10589
sum = 0
print(len(str(sum)))
    
while True:
    for i in range(len(str(number))):
        sum += int(str(number)[i])
        print(sum)
    number = sum
    if len(str(number))==1:
        break
     

print()