# Prime Number Checker
# Note: this function has potential to deal with big numbers. 
# However due to the python's efficiency problem, it may take long time to process.

def prime_number_checker():
    number_input = input("Please input a number: ")
    number = int(number_input)
    prime_list = []
    # for i in range(1, number):
    for i in range (1, 10**len(number_input)):
        if number % i == 0:
            prime_list.append(i)
    if prime_list == [1, number]:
        print("Prime")
    else:
        print("Composite")

prime_number_checker()