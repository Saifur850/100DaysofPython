print("Welcome to the love calculator! ")
name1= input("What is your name? ")
name2= input("What is their name? ")

name1_lower= name1.lower()
name2_lower= name2.lower()

t=0
r=0
u=0
e=0
l=0
o=0
v=0

t+= name1_lower.count('t')
t+= name2_lower.count('t')

r+= name1_lower.count('r')
r+= name2_lower.count('r')

u+= name1_lower.count('u')
u+= name2_lower.count('u')

e+= name1_lower.count('e')
e+= name2_lower.count('e')

l+= name1_lower.count('l')
l+= name2_lower.count('l')

o+= name1_lower.count('o')
o+= name2_lower.count('o')

v+= name1_lower.count('v')
v+= name2_lower.count('v')

true= str(t+r+u+e)
love= str(l+o+v+e)

truelove= int(true+love)

if truelove<10 or truelove>90:
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove>40 and truelove<50:
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")

