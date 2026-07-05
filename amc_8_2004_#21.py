from fractions import Fraction

spinner_a = [1,2,3,4]
spinner_b = [1,2,3]
total_cases = 0
favorable_cases = 0

for a in spinner_a:
    for b in spinner_b:
        
        total_cases = total_cases + 1

        if (a*b) % 2 == 0:
            favorable_cases = favorable_cases + 1

answer = Fraction(favorable_cases, total_cases)

print(answer)
