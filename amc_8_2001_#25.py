four_digit_list = [2,4,5,7]
all_possible_numbers = []

for a in four_digit_list:
    three_digit_list = four_digit_list.copy()
    three_digit_list.remove(a)
    for b in three_digit_list:
        two_digit_list = three_digit_list.copy()
        two_digit_list.remove(b)
        for c in two_digit_list:
            one_digit_list = two_digit_list.copy()
            one_digit_list.remove(c)
            for d in one_digit_list:
                one_digit_list = one_digit_list

                four_digit_number = 1000*a + 100*b + 10*c + d     

                #print(four_digit_number)
                all_possible_numbers.append(four_digit_number)

print(all_possible_numbers, len(all_possible_numbers))

for a in all_possible_numbers:
    #all_but_one_possible_numbers = all_possible_numbers.copy()
    #all_but_one_possible_numbers.remove(a)

    #print("len",len(all_but_one_possible_numbers))
    #all_but_one_possible_numbers.remove(a)
    
    for b in all_possible_numbers:
        if (a % b == 0) and (a != b):
            print(a,b)




            

