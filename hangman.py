import random
import sys

word_choices = ["Basketball", "Soccer", "Computer", "Chair", "Tree", "Movie", "Teacher", 
                "Doctor", "Mother", "Friend", "Artist", "Child", "Player", "Chef", "Pilot", 
                "Police officer", "School", "Hospital", "Library", "Park", "City", "Country",
                  "Beach", "Mountain", "Airport", "Restaurant", "Computer", "Book", "Car", 
                  "Phone", "Chair", "Table", "Dog", "Cat", "Tree", "Flower", "Sun", "Moon",
                    "River", "Ocean", "Rain", "Sky", "Cloud", "Wind", "Star", "Fire", "Love", 
                    "Happiness", "Freedom", "Time", "Knowledge", "Peace", "Courage", "Honesty", 
                    "Justice", "Friendship"]

chosen_word = random.choice(word_choices).lower()
correct_letters = 0
word_length = len(chosen_word)
wrong_guesses_remaining = word_length*2

guessed_letters = [] #AI's idea to help with the __d_s_ part

print("Your word has", word_length, "letters")

while correct_letters < word_length:

    guess = input("Guess one lowercase letter that may be in the word: ")

    if guess not in guessed_letters: #AI's idea so that i can print the guessed words so people don't repeat
        guessed_letters.append(guess)

    if guess in chosen_word:

        for position, letter in enumerate(chosen_word): # Ai's idea to use enumerate so that if a letter appear twice, it would be seen twice
            if letter == guess:
                print("Found at position", position + 1)
                correct_letters = correct_letters + 1

    else:
        print(guess, "is not in the word. Try again")
        wrong_guesses_remaining = wrong_guesses_remaining - 1
        print("You have", wrong_guesses_remaining, "wrong guesses remaining")
    
    if wrong_guesses_remaining == 0:
        print("GAME OVER. You took too many guesses!")
        print("The word was", chosen_word)
        sys.exit()

    progress = ""                       #Ai's idea which i probably could've come up with.
    for letter in chosen_word:
        if letter in guessed_letters:
            progress = progress + letter
        if letter not in guessed_letters:
            progress = progress + "_"
    print(progress)

    print("Letters you already guessed", guessed_letters)


print("Good Job! You figured out all the letters with", wrong_guesses_remaining, "wrong guesses remaining")
print("The word was", chosen_word)