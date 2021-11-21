# High Score

def high_score():
    scores = input("input your list:\n").strip().replace(",", " ").split(" ")
    highest = 0
    for i in scores:
        if i == "":
            scores.remove(i)
    for j in scores:
        if int(j) > highest:
            highest = int(j)
    print(highest)

high_score()