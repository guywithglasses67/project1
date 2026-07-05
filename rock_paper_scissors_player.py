import random

choices = ["Rock", "Paper", "Scissors"]
bot_choice = random.choice(choices)

user_choice = input("What do you choose: ")

while user_choice == bot_choice:
    user_choice = input("You Tied! What do you choose: ")
    bot_choice = random.choice(choices)

#If user_choice is Rock
if user_choice == "Rock" and bot_choice == "Scissors":
    print("You Win! Bot Chose: ", bot_choice)
elif user_choice == "Rock" and bot_choice == "Paper":
    print("Bot Wins! Bot Chose: ", bot_choice)

#If user_choice is Paper
if user_choice == "Paper" and bot_choice == "Scissors":
    print("Bot Wins! Bot Chose: ", bot_choice)
elif user_choice == "Paper" and bot_choice == "Rock":
    print("You Win! Bot Chose: ", bot_choice)

#If user_choice is Scissors
if user_choice == "Scissors" and bot_choice == "Rock":
    print("Bot Wins! Bot Chose: ", bot_choice)
elif user_choice == "Scissors" and bot_choice == "Paper":
    print("You Win! Bot Chose: ", bot_choice)
