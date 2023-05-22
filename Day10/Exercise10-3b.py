def add_num(n1,n2):
    """This method will add two numbers; n1 and n2"""
    return n1+n2

def sub_num(n1,n2):
    return n1-n2

def mul_num(n1,n2):
    return n1*n2

def div_num(n1,n2):
    return n1/n2

operations={
    "+": add_num,
    "-": sub_num,
    "*": mul_num,
    "/": div_num
}

def calculator():
    first_number= int(input("What is the first number? "))

    for symbol in operations:
        print(symbol)
    loop=True
    while loop:
        operation_symbol= input("Pick an operation from list above: ")
        second_number= int(input("What is the next number? "))

        operation= operations[operation_symbol]
        answer= operation(first_number,second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        confirmation= input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculator: ")
        if confirmation=='n':
            loop=False
            calculator()
        else:
            first_number=answer

calculator()

