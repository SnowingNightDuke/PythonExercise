# Leap Year

def leap_year(year):
    if (year%4 == 0):
        if (year%100==0) and (year%400!=0):
            return print("not leap")
        else: 
            return print("leap")
    else:
        return print("not leap")


leap_year(int(input("Please input a year: ")))