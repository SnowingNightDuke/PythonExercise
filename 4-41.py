# Heads or Tails
import random

def heads_or_tails():
    result = random.random()
    if result < 0.5:
        print("Heads")
    else:
        print("Tails")

heads_or_tails()