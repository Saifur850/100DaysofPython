student_heights= input("Input a list of students height: ").split()
for n in range(0, len(student_heights)):
    student_heights[n]= int(student_heights[n])

# print(student_heights)

total_height= 0
for height in student_heights:
    total_height+= height
# print(total_height)

total_student=0
for student in student_heights:
    total_student+=1
# print(total_student)

average= total_height/total_student

print(round(average,2))
