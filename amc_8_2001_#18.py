total_rolls = 0
multiple_of_5 = 0

for dice_1 in range(1,7):
    for dice_2 in range(1,7):

        total_rolls = total_rolls + 1
        condition = (dice_1 * dice_2) % 5 == 0
        if condition:
            multiple_of_5 = multiple_of_5 + 1

f1 = (multiple_of_5 / total_rolls) * 100
print(f1)
