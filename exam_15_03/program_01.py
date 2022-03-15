# Finding the sum of all digits of a number until the sum becomes a single digit.
# Examples. 10589=>5 , 121=>4, 99=>9, 10=>1
# number = 10589

a='10589'
while(len(a)>1):
# print(len(a))
    for i in a:
        sum = int(sum) + int(i)
        # print(sum)
    a = str(sum)
print(a)



