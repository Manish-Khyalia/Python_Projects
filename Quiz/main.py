from art import logo
print(logo)
auction_complete = False
Auction_dictionary = {}
name = ""
while  not auction_complete :
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    Any_other = input("Are there any other biddeers? Type 'yes' or 'no'.\n").lower()
    print("\n"*30)
    if Any_other == "no" :
        auction_complete = True
    Auction_dictionary[name] = bid
highest = 0
top_bidder = ""
for name in Auction_dictionary :
    if Auction_dictionary[name] > highest :
        highest = Auction_dictionary[name]
        top_bidder = name
print(f"The winner is {top_bidder} with a bid of ${highest}")