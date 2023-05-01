marks= input("Input the mark of students: ").split()

total_student=0
for student in marks:
    total_student+=1

highest_mark=marks[0]
for n in range(0,total_student):
    if marks[n]>highest_mark:
        highest_mark=marks[n]
    
print(highest_mark)