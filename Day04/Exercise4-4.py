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

choice= int(input("What do you chose? Type 0 for Rock, type 1 for Paper or type 2 for Scissor: "))

random_number= int(random.randint(0,2))

if choice==0:
    print(Rock)
    if random_number==0:
        print(f"{Rock} \n Draw")
    elif random_number==1:
        print(f"{Paper} \n Lose!!!")
    elif random_number==2:
        print(f"{Scissor} \n Win!!!")
    

elif choice==1:
    print(Paper)
    if random_number==0:
        print(f"{Rock} \n Win!!")
    elif random_number==1:
        print(f"{Paper} \n Draw!!!")
    elif random_number==2:
        print(f"{Scissor} \n Lose!!!")


elif choice==2:
    print(Scissor)
    if random_number==0:
        print(f"{Rock} \n Lose")
    elif random_number==1:
        print(f"{Paper} \n Win!!!")
    elif random_number==2:
        print(f"{Scissor} \n Draw!!!")