# odd or even

def odd_or_even(n):
    result = "even"
    if n%2 != 0:
        result = "odd"
    return print(result)
number = int(input("Please input a number: "))


odd_or_even(number)