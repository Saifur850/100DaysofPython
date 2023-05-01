import random

test_seed= int(input("Create a seed number: "))
random.seed(test_seed)

random_number= random.randint(0,1)
print(random_number)

if random_number== 1:
    print("Head")
else:
    print("Tail")