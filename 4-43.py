# Banker Roulette

import random

def banker_roulette():
    names = input("Please input bankers' name:\n")
    banker_list = names.replace(" ","").split(",")
    number = random.randint(0, len(banker_list)-1)
    print(f"{banker_list[number]} is going to pay the bill!")

# banker_roulette()

# Alternatively, 
def alter_roulette():
    names = input("Please input bankers' name:\n").replace(" ", "").split(",")
    print(f"{random.choice(names)} is going to pay the bill!")


alter_roulette()