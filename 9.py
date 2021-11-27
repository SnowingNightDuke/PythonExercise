# Silent Bidder - secret auction

def secret_auction():
    
    flag = "yes"
    bid_dict = {}
    highest_bid = 0
    highest_bid_name = ""

    while flag == "yes" or flag == "Yes" or flag == "Y" or flag == "y":
        name = input("Please input your name: ")
        bid = float(input("Please input your bid: "))
        bid_dict[name] = bid
        flag = input("Anyone else? ")

    for key in bid_dict:
        if bid_dict[key] > highest_bid:
            highest_bid_name = key
            highest_bid = bid_dict[key]
    
    print(f"Winner bidder: {highest_bid_name} with highest bid: ${highest_bid}")

secret_auction()