import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# word_list= ['saifur', 'arifa', 'nicolota']
from words import word_list
choosen= random.choice(word_list)

print(f"The choosen word is {choosen}")

emp_list= []
for list in choosen:
    emp_list.extend("_")

print(emp_list)

lives=0
end_of_game= False

while not end_of_game:
    guess= input("\n\nGuess a letter: ").lower()
    n=0
    if guess in emp_list:
        print("You have already guessed that letter.")
    for letter in choosen:
        if letter==guess:
            emp_list[n]=guess             
        n+=1
    if "_" not in emp_list:
        end_of_game=True
        print("You won!")
    
        
    print(emp_list)
    
    if guess not in choosen:
        
        lives+=1
    print(stages[lives])  
    if lives==6 :
        end_of_game=True
        print("You lose!!")
    
    

  