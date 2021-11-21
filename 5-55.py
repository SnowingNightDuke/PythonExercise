# Password Generator
import random
import string

def password_generator():
    letter_numbers = int(input("How many latters do you want? "))
    numbers_numbers = int(input("How many numbers do you want? "))
    symbols_numbers = int(input("How many symbols do you want? "))
    password = []
    for i in range(letter_numbers):
        password.append(random.choice(string.ascii_letters))
    for j in range(numbers_numbers):
        password.append(random.choice(string.digits))
    for k in range(symbols_numbers):
        password.append(random.choice(string.punctuation))
    random.shuffle(password)
    print(''.join((password)))

password_generator()
