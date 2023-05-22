import os
data={}

def check_highest_bidder(bidder):
    for data in bidder:
        highest=0
        winner=""
        bid= bidder[data]
        if bid>highest:
            highest=bid
            winner= data
    print(f"The winner is {winner} with a bid of ${highest}")
loop= True
while loop:
    name=input("What is your name? ")
    bid=int(input("What is your bed? "))
    data[name]=bid
    type= input("Is there any bidder? Type 'yes' if any, else type 'no': ")
    os.system('cls')
    check_highest_bidder(data)
    if type=='no':
        loop=False
    
    
