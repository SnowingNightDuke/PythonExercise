# 
def ride():
    height = input("Height > 120 cm? y or n: ")
    bill = 0
    if height == "n":
        print("Can't ride")
    else:
        age = int(input("Age"))
        if age < 12:
            bill += 5
        elif (age < 18) and (age > 12):
            bill += 7
        elif (age > 18) and (not (age < 55 and age >45)):
            bill += 12
        photo = input("Do you want photos? ")
        if photo == "y":
            bill += 3
    return print(bill)

ride()