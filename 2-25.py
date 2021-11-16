def calculator(bill, tips, people):
    return str(round(bill*(1+(tips/100))/people, 2))

print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? $ "))
tips = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
print("Each person should pay: $" + calculator(bill, tips, people))
