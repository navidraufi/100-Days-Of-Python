from os import system


bidders = []

print("Bienvenidos a la programo de auciones.")

def add_bidder(result):
    new_bidder= {}
    
    name = input("Entre tus nombre: ")
    bid = int(input("Cual es tu dinero?: $"))
    
    new_bidder["Name"] = name
    new_bidder["Bid"] = bid
    
    result.append(new_bidder)
    
are_there_bidders = True

add_bidder(bidders)

while are_there_bidders:
        
    more_bidders = input("Are there more bidders? 'Yes' or 'No' : ").lower()
    if more_bidders == "yes":
        system("cls")
        add_bidder(bidders)
    elif more_bidders == "no":
        system("cls")
        are_there_bidders = False
        winner = {
            "Name": "",
            "Bid": 0 
        }
        for bid in bidders:
            if bid["Bid"] > winner["Bid"]:
                winner["Name"] = bid["Name"]
                winner["Bid"] = bid["Bid"]
                
        print(f"The winner is {winner['Name']} with a bid of ${winner['Bid']}.")
        