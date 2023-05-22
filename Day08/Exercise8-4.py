def caesar(type,message,shift):
    new_mess=""
    for letter in message:
        if letter in alphabet:
            if type=="encode":
                n=alphabet.index(letter)
                new_mess+=alphabet[n+shift]
            elif type=="decode":
                n=alphabet.index(letter)+26
                new_mess+=alphabet[n-shift]
        else:
            new_mess+=letter

    print(new_mess)


alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 
           'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

loop= True
while loop==True:
    direction= input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text= input("Type your message: \n")
    shift= int(input("Type the shift number: \n"))
    shift=shift%26
    caesar(direction,text,shift)

    conformation= input("Type 'yes' if you want to go again, else type 'no'! ")

    if conformation=='no':
        loop=False
        
