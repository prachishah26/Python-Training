# Check if the given number is prime or not
import math
number = 7
n = 2
def prime(number,n):
    if number == 1 :
        return("unique value")

    if(n>math.sqrt(number)):
        return "prime"
    elif number % n == 0:
        return "not prime"
    n += 1
    return prime(number,n)
            
print(prime(number,n))

# print(5%0)












