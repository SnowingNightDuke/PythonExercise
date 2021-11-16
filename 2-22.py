def bmi(h,w):
    return round(w/h**2) 

h=float(input("height: "))
w=float(input("weight: "))
print(bmi(h,w))