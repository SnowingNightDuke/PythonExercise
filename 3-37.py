# Treasure Island

def treasure_island():
    print("Welcome to Treasure Island.\n Go left or right?\n")
    step1 = input().lower()
    if step1 == "left":
        print("Swim or wait?\n")
        step2 = input().lower()
        if step2 == "wait":
            print("Which door? red, blue or yellow?\n")
            step3 = input().lower()
            if step3 == "yellow":
                print("You win")
            else:
                print("Game Over.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")

treasure_island()