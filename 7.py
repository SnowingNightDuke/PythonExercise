# Hangman
import random

life = 8
succeed = False
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
question = []
chosen_word_array = []
for i in range(len(chosen_word)):
    question.append("_")
for i in chosen_word:
    chosen_word_array.append(i)
    
print(*question)

while life > 0 and not succeed:
    guess = input("Please guess a letter: ").lower()
    if guess in chosen_word_array:
        print("Correct")
        print(f"Your life remains: {life}")
        question[chosen_word_array.index(guess)] = guess
        chosen_word_array[chosen_word_array.index(guess)] = "_"
        print(*question)
        if "_" not in question:
            succeed = True
            print("You won the game")
    else:
        print("Wrong")
        life -= 1
        print(f"Your life remains: {life}")
        print(*question)
while life == 0:
    print("You lost")