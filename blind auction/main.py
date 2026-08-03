from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidding = True
bidding_dict = {
}

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidding_dict[name] = bid
    continue_bidding = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if continue_bidding == "yes":
        print("\n" * 20)
    else:
        bidding = False

highest_bid = 0
highest_bidder = ""

for bid in bidding_dict:
    highest_bidder = bid
    for bidder in bidding_dict:
        if bidding_dict[bidder] > highest_bid:
            highest_bid = bidding_dict[bidder]
            highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
