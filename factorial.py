from count_prob_formulas import stars_and_bars


n = 6
factorial = 1

for i in range(n):
    factorial = factorial * ( i+1 )
    print(i, i+1, factorial)
print(f"Factorial of {n} is {factorial}")


n = 6
temp = 1
while n > 1:
    temp = temp * n
    n = n - 1
    print(n)

factorial = temp

print(factorial)

stars = stars_and_bars(5, 3)
print("stars and bars", stars)
