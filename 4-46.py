# Rock Paper Scissors
import random

def rock_paper_scissors():
    go_list = ["Rock", "Paper", "Scissors"]
    user_go = input("Please select your go (Rock, Paper, Scissors): \n")
    computer_go = random.choice(go_list)
    if user_go == "Rock" and computer_go == "Scissors":
        print("You win")
    elif user_go == "Rock"