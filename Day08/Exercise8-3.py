def encrypt(message,number):
    new_mess=""
    
    for letter in message:
        n=alphabet.index(letter)
        new_mess+=alphabet[n+number]
        
    print(new_mess)

def decrypt(message,number):
    new_mess=""
    for letter in message:
        n= alphabet.index(letter)+26
        new_mess+=alphabet[n-number]
    print(new_mess)


alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 
           'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

direction= input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

text= input("Type your message: \n")
shift= int(input("Type the shift number: \n"))

if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("Please type encode or decode. ")







