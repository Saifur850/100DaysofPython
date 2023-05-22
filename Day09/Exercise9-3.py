import os
# os.system('cls')
data={}

winner_name=""
def find_higest_bidder(bidder):
    highest=0
    for datas in bidder:
        bid=bidder[datas]
        if bid>highest:
            highest= bidder[datas]
            winner_name= datas
    print(f"The winner is {winner_name}, with a bid of ${highest}")

loop=True
while loop:
    name= input("What is your name? ")
    bid= int(input("What is your bid? "))
    any= input("Are there any bidder? Type 'yes' or 'no': ")
    data[name]= bid
    os.system('cls')
    if any=='no':
        loop= False

find_higest_bidder(data)

        


