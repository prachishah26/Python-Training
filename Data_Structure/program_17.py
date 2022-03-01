# Print reverse string using recursion

A = "helloworld"

n = len(A)
def rev_str(A, n):
    n -= 1
    if n == 0:
        return A[n]
    return A[n] + rev_str(A,n) 

print(rev_str(A,n))