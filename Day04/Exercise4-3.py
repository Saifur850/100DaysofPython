row1=["O","O","O"]
row2=["O","O","O"]
row3=["O","O","O"]
map= [row1,row2,row2]

print(f"{row1}\n{row2}\n{row3}")

position= input("Where do you want to put the X? ")

x= int(position[0])
y= int(position[1])

if y==1:
    row1[x-1]= "X"
elif y==2:
    row2[x-1]= "X"
elif y==3:
    row3[x-1]= "X"

print(f"{row1}\n{row2}\n{row3}")


