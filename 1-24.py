def life_in_weeks(age):
    day = (90-int(age))*365
    # week = day//7
    week = (90-int(age))*52
    # month = day//30
    month = (90-int(age))*12
    return f"You have {day} days, {week} weeks, and {month} months left"

print(life_in_weeks(input("what is your age? ")))