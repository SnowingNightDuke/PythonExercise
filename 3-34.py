# Pizza Order Practice

def pizza():
    bill = 0
    size = input("What size of Pizza do you want? ")
    if size == "small":
        bill = 15
    elif size == "medium":
        bill = 20
    elif size == "large":
        bill = 25
    pepperoni = input("Do you want Peppoeroni for you pizza? y or n ")
    if pepperoni == "y":
        if size == "small":
            bill += 2
        else:
            bill += 3
    cheese = input("Do you want cheese for it? y or n ")
    if cheese == "y":
        bill += 1
    return print(bill)


pizza()