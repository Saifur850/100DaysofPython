import random
import os
cards= [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
user=[]
computer=[]
def deal_card():
    return random.choice(cards)

def calculate_score(list):
    sum=0
    for n in list:
        sum+=n
    return sum

def compare(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

def user_game(user_score,computer_score):
    while computer_score<17:
        y=computer.append(deal_card())
        computer_score= calculate_score(computer)
        # print(computer_score)
    print(f"Your final hand: {user}, final score: {user_score}")
    computer_score= calculate_score(computer)
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    x= compare(user_score,computer_score)
    if x==1:
        print("User win")
    elif x==-1:
        print("Computer win")
    else:
        print("Draw")
    
def repeat():  
    user_score= calculate_score(user)
    computer_score= calculate_score(computer)
    # print(user_score)
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first score {computer[0]}")
    if user_score==21:
        print(f"Your final hand: {user}, final score: {user_score}")
        print(f"Computer's final hand: {computer}, final score: {computer_score}")
        print("user wins")
    elif computer_score==21:
        print(f"Your final hand: {user}, final score: {user_score}")
        print(f"Computer's final hand: {computer}, final score: {computer_score}")
        print("computer wins")
    elif user_score>21:
        user_game(user_score,computer_score)
    else:
        confirm2= input("Do you want to take another card? Type 'y' or 'n': ")
        if confirm2=='y':
            user.append(deal_card())
            repeat()
        else:
            # the computer score will increase
            user_game(user_score,computer_score)

loop =True
while loop:    
    confirmation= input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    os.system('cls')
    if confirmation=='y':       
        for n in range(0,2):    
            user.append(deal_card())
            computer.append(deal_card()) 
        repeat()
    else:
        loop=False
    user=[]
    computer=[]
