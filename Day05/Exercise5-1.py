student_heights= input("Input a list of students height: ").split()
for n in range(0, len(student_heights)):
    student_heights[n]= int(student_heights[n])

print(student_heights)

sum=0
for n in range(0, len(student_heights)):
    sum+=student_heights[n]
average= sum/ len(student_heights)

print(average)