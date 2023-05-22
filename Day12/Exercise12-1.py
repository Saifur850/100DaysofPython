import random

print("Welcome to the number guessing game!!!")
print("I am thinking a number between 1 to 100.")
loop=True
while loop:
    difficulty= input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty=='easy':
        attempt=10
        print(f"You have {attempt} attempts remaining to guess the number. ")
        loop=False
    elif difficulty=='hard':
        attempt=5
        print(f"You have {attempt} attempts remaining to guess the number. ")
        loop=False
    else:
        print("Type correctly")
random_number= random.randint(1,100)
print(random_number)


def guess_again(attempt):
    if attempt>0:
        number= int(input("Make a guess: "))
        if number!=random_number and number>random_number:
            print("It's high!")
            attempt-=1
            print(f"You have {attempt} attempts remaining to guess the number. ")
            guess_again(attempt)
        elif number!=random_number and number<random_number:
            print("It's Low!")
            attempt-=1
            print(f"You have {attempt} attempts remaining to guess the number. ")
            guess_again(attempt)
        else:
            print("You win")
    else:
        print("Game Over")

guess_again(attempt)