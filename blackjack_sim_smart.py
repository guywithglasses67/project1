import random

bot_total = 0
user_total = 0
bot_decision = "Hit"
user_decision = "Hit"

def new_card():
    card = random.randint(1,10)
    return card

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

while 21-int(bot_total) > random.randint(2,7):
    bot_total = bot_total + int(new_card())

print("The Bot's final score is: ", bot_total)

if user_total > 21:
    print("Bot Wins! (You Busted)")
elif bot_total > 21:
    print("You Win! (Bot Busted)")
elif bot_total > user_total:
    print("Bot Wins")
elif bot_total < user_total:
    print("You Win!")
else:
    print("You Tied!")