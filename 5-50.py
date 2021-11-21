# Average Height

def average_height():
    heights = input("input your list:\n").strip().replace(",", " ").split(" ")
    total = 0
    for i in heights:
        if i == "":
            heights.remove(i)
    for j in heights:
        total += float(j)
    print(f"The average height is: {round(total/len(heights), 2)}")

average_height()
