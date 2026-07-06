#A Blackjack game in which you can play against a robot where aces are worth 1.
#You and the Bot each start with $100. You will play a round of Blackjack. Whoever loses that round loses 1/2 of 
# their money. Whoever wins gets 1/4 of the other's money. Once someone has $15 of less, the game ends.
#Your final earnings will be announced. You would make a profit if your final earnings are positive. 
#You would make a loss if your final earnings are negative.
#Because one person gets 1/4 and the other loses 1/2, the total money will go down over time. That money
#goes to the house.


import random
import sys

house_money = 0
bot_money = 100
user_money = 100
bot_total = 0
user_total = 0
bot_decision = "Hit"
user_decision = "Hit"

def new_card():
    card = random.randint(1,10)
    return card
while user_money >15 and bot_money >15:

    user_total = 0
    bot_total = 0

    print("You have $", round(user_money, 2))
    print("The bot has $", round(bot_money, 2))

    first_card = new_card()
    user_total = user_total + first_card

    print("Your first card is a", str(first_card))

    user_decision = input("Hit or Stay: ")

    while user_decision == "Hit":
    
        user_total = user_total + int(new_card())
        print("Your current total is: ", user_total)

        if int(user_total) > 21:
            break

        user_decision = input("Hit or Stay: ")

    if user_total <= 21:
        print("Your final total is: ", user_total)
    else: 
        print("You Busted")

    #-------------Bot Code---------------#

    bot_total = new_card()

    while 21-int(bot_total) > random.randint(4,7):
        bot_total = bot_total + int(new_card())

    print("The Bot's final score is: ", bot_total)

    if user_total > 21:
        print("Bot Wins this round! (You Busted)")
        user_money = user_money/2
        bot_money = bot_money + user_money

    elif bot_total == 21:
        print("Bot got BLACKJACK for this round")
        user_money = user_money/2
        bot_money = bot_money + user_money

    elif user_total == 21:
        print("You got BLACKJACK for this round")
        bot_money = bot_money/2
        user_money = user_money + bot_money/2
    elif bot_total > 21:
        print("You Win this round! (Bot Busted)")
        bot_money = bot_money/2
        user_money = user_money + bot_money/2
    elif bot_total > user_total:
        print("Bot Wins this round")
        user_money = user_money/2
        bot_money = bot_money + user_money/2

    elif bot_total < user_total:
        print("You Win this round!")
        bot_money = bot_money/2
        user_money = user_money + bot_money/2
    else:
        print("You Tied! Both of you keep your earnings or losses!")
        print("Your total money is: $", user_money-100)
        print("The Bot's total money is: $", bot_money-100)
        sys.exit()


    print("------------")

if bot_money < 15:
    print("You won the game! You earned: $", round(user_money-100, 2))
if user_money < 15:
        print("You lost the game! You lost: $", round(abs(user_money-100), 2))
print("The house earned: $", round(200-bot_money-user_money, 2))