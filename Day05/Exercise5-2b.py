marks= input("Input the mark of students: ").split()

highest=marks[0]
for score in marks:
    if score>highest:
        highest=score

print(highest)
