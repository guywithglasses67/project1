def solve_factorial(a):
    factorial = 1
    while  a > 1:
        factorial = factorial * a
        a = a - 1
    return factorial

def choose(n, r):
    return (solve_factorial(n))/(solve_factorial(r)*(solve_factorial(n-r)))

def stars_and_bars(n, k):
    return choose(n+k-1, k-1)

print(stars_and_bars(5, 3))


