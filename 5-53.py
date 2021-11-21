# Adding Even Numbers

def add_even_numbers():
    total = 0
    for i in range(1,101):
        if i%2==0:
            total+=i
    print(total)

add_even_numbers()