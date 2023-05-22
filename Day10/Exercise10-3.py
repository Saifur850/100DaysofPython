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

first_number= int(input("What is the first number? "))

for symbol in operations:
    print(symbol)

operation_symbol= input("Pick an operation from list above: ")
second_number= int(input("What is the second number? "))

operation= operations[operation_symbol]
first_answer= operation(first_number,second_number)

print(f"{first_number} {operation_symbol} {second_number} = {first_answer}")

operation_symbol= input("Pick another operation from list above: ")
third_number= int(input("What is the third number? "))
operation= operations[operation_symbol]
second_answer= operation(operation(first_number,second_number),third_number)

print(f"{first_answer} {operation_symbol} {third_number} = {second_answer}")