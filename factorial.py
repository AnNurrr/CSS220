# Ainur
# 3/12/24
# CSS 220 Module 9

#Factorial Recursion Example

# 5! 5*4*3*2*1

def factRecursion(n):
    # Base case: 1! =1
    if n==1:
        return 1
    # Recursive case: n! = n*(n-1)!
    else:
        return n*factRecursion(n-1)

print(factRecursion(5))