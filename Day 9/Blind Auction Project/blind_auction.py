from art import logo

print(logo)
print("Welcome to the secret auction program.")

users_and_bids = {}

def user_and_bid():
    user = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    users_and_bids[user] = bid
    silent_auction()

def silent_auction():
    add = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if add == "yes":
        print("\n" * 10)
        print(users_and_bids)
        user_and_bid()
    elif add == "no":
        print("\n" * 10)
        highest_bid()
    else:
        print("\n" * 10)
        print("Wrong input. Please enter 'yes' or 'no'.")
        silent_auction()

def highest_bid():
    top_bid, top_user = max((value, key) for key, value in users_and_bids.items())
    print(f"The winner is {top_user} with a bid of ${top_bid}.")

user_and_bid()