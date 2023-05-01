import random

test_seed= int(input("Create a seed number: "))
random.seed(test_seed)

name_str= input("Write names separated with a , and a space in between: ")
name_list= name_str.split(', ')


x= len(name_list)

y= random.randint(0,x-1)

print(f"{name_list[y]} is going to pay the bill.")



