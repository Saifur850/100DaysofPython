from game_data import data
import random
import os

def compare(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    
score=0
def loop(score):

    data_list=[]
    for n in range(0,2):
        data_list.append(random.choice(data))
    
    # print(data_list)


    data1= data_list[0]
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}")
    # print(data1['follower_count'])

    data2= data_list[1]
    print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}")
    # print(data2['follower_count'])

    check= input("Who has more followers? Type 'A' or 'B': ")

    comparing= compare(data1['follower_count'],data2['follower_count'])

    if comparing==1 and check=="A":
        os.system('cls') 
        score+=1
        print(f"You are right! Current score: {score}")
        loop(score)
    elif comparing==-1 and check=="B":
        os.system('cls')
        score+=1
        print(f"You are right! Current score: {score}")
        loop(score)
    else:
        print(f"Wrong. The final score is {score}")

loop(score)