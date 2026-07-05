favorable_outcomes = 0
total_outcomes = 0

for coin_1 in range(1, 3):
    for coin_2 in range(1, 3):
        for coin_3 in range(1, 3):
            for coin_4 in range(1, 3):

                total_outcomes = total_outcomes + 1
                
                number_of_heads = 0
                number_of_tails = 0

                if coin_1 == 1:
                    number_of_heads = number_of_heads + 1
                else:
                    number_of_tails = number_of_tails + 1
                if coin_2 == 1:
                    number_of_heads = number_of_heads + 1
                else:
                    number_of_tails = number_of_tails + 1
                if coin_3 == 1:
                    number_of_heads = number_of_heads + 1
                else:
                    number_of_tails = number_of_tails + 1
                if coin_4 == 1:
                    number_of_heads = number_of_heads + 1
                else:
                    number_of_tails = number_of_tails + 1

                if number_of_heads >= number_of_tails:
                    favorable_outcomes = favorable_outcomes + 1

print(f"{favorable_outcomes}/{total_outcomes}")