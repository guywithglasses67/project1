favorable_outcomes = 0
total_outcomes = 0

for coin_1 in range(2):
    for coin_2 in range(2):
        for coin_3 in range(2):
            for coin_4 in range(2):

                total_outcomes = total_outcomes + 1

                number_of_tails = coin_1 + coin_2 + coin_3 + coin_4
                number_of_heads = 4 - number_of_tails

                if number_of_heads >= number_of_tails:
                    favorable_outcomes = favorable_outcomes + 1

print(f"{favorable_outcomes}/{total_outcomes}")