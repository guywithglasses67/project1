# Problem: Camy made a list of every possible distinct five-digit positive integer that can be formed using 
# each of the digits $1$, $3$, $4$, $5$ and $9$ exactly once in each integer. What is the sum of the integers
#  on Camy's list?

five_digit_list = [1, 3, 4, 5, 9]
total_sum = 0

for a in five_digit_list:
    four_digit_list = five_digit_list.copy()
    four_digit_list.remove(a)
    for b in four_digit_list:
        three_digit_list = four_digit_list.copy()
        three_digit_list.remove(b)
        for c in three_digit_list:
            two_digit_list = three_digit_list.copy()
            two_digit_list.remove(c)
            for d in two_digit_list:
                one_digit_list = two_digit_list.copy()
                two_digit_list.remove(d)
                for e in one_digit_list:
                    one_digit_list = one_digit_list

                five_digit_number = 10000*a + 1000*b + 100*c + 10*d + e
                total_sum = total_sum + five_digit_number

print(total_sum)
