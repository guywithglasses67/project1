from math import sqrt

def is_prime(n):
    greatest_tester = int(sqrt(n))
    for i in range(2, greatest_tester+1):
        if n % i == 0:
            return "Composite"
    return "Prime"
    
print(is_prime(1))