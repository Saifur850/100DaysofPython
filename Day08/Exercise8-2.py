def prime(num):
    flag=0
    for n in range(2,num):
        if num%n==0:
            flag=1
    if flag==1:
            print("It's a not prime number.")
    else:
            print("It's a prime number.")


number= int(input("Input any number to check whether it's a prime number or not: "))

prime(number)