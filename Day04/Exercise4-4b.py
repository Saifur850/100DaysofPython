import random

Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissor= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
RPS= [Rock,Paper,Scissor]
user_number= int(input("What do you chose? Type 0 for Rock, type 1 for Paper or type 2 for Scissor: "))

computer_number= int(random.randint(0,2))
print("You choose: ")
print(RPS[user_number])
print("Computer choose: ")
print(RPS[computer_number])

if user_number== computer_number:
    print("Draw!!")
elif user_number==0 and computer_number==1:
    print("Computer wins!!")
elif user_number==0 and computer_number==2:
    print("You win")
elif user_number==1 and computer_number==0:
    print("You win")
elif user_number==1 and computer_number==2:
    print("Computer wins")
elif user_number==2 and computer_number==0:
    print("Computer wins")
elif user_number==2 and computer_number==1:
    print("You win")
else:
    print("Invalid Input!!")

