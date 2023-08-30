from rel import clear
dict = {}
bid_finished = False
def highest_price():
    higher_price = 0
    for price in dict:
        dict[name] = price
        if price > higher_price:
            higher_price = price
    print(f"this is the winner {name}")
       


while not bid_finished:
    name = input("enter your name ")
    price = int(input("enter bid price $"))
    dict[name] = price
    other_bidders = input("is there any other bidders? type 'yes' or 'no' ")
    if other_bidders == "no":
        bid_finished = True
        highest_price(dict)
    elif other_bidders == "yes":
        clear()

