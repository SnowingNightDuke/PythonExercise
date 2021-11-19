# Love Calculator

def love_calculator():
    first_digit = 0
    last_digit = 0
    first_name = input("Please input the first name").replace(" ", "")
    second_name = input("Please input the second name").replace(" ", "")
    name = first_name + second_name
    for i in name.lower():
        if i == "t" or i =="r" or i == "u" or i == "e":
            first_digit += 1
    for j in name.lower():
        if j == "l" or j == "o" or j == "v" or j == "e":
            last_digit += 1

    percentage = first_digit * 10 + last_digit
    return print(f"your percentage is {percentage}%")

love_calculator()