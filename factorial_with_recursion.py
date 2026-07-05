def new_factorial(n):
    if n>1:
        n = n*(new_factorial(n-1))
    return(n)

print(new_factorial(5))