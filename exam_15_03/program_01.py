# Finding the sum of all digits of a number until the sum becomes a single digit.
# Examples. 10589=>5 , 121=>4, 99=>9, 10=>1
# number = 10589

number = 22
if number == 0:
    print(0)
elif number%9 == 0:
    print("Sum is : ",9)
elif number%9 != 0:
    print("Sum is : ",number%9)
else :
    print("Enter a valid number")
