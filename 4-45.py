# Treasure Map

def treasure_map():
    row1 = ["O", "O", "O"]
    row2 = ["O", "O", "O"]
    row3 = ["O", "O", "O"]
    pick = input("Please input your pick: ")

    maps = [row1, row2, row3]
    maps[int(pick[0])-1][int(pick[1])-1] = "X"
    for i in maps:
        print(i)
        print("\n")
treasure_map()