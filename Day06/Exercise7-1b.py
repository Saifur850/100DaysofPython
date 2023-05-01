import random

word_list= ['saifur', 'nicolota', 'jackson']

choosen= random.choice(word_list)

guess= input("Guess a letter: ").lower()

for letter in choosen:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")