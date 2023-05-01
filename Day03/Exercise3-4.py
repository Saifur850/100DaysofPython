print("Welcome to Pyhone Pizza Deliveries!")
size= input("What size pizza do you want? S, M or L ")
add_pepperoni= input("Do you want peppernoni? Y or N ")
extra_cheese= input("Do you want extra cheese? Y or N ")

if size=='S':
    bill= 15
    if add_pepperoni== 'Y':
        bill=17
elif size=='M':
    bill= 20
    if add_pepperoni== 'Y':
        bill=23
elif size=='L':
    bill= 25
    if add_pepperoni== 'Y':
        bill=28

if extra_cheese== 'Y':
    bill+=1

print(f"The total bill is ${bill}")