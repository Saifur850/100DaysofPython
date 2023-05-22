student_scores={
    "Harry": 81,
    "Rom": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades={}
for scores in student_scores:
    if student_scores[scores]<=100 and student_scores[scores]>89:
        student_grades[scores]= "Excellent"
    elif student_scores[scores]<=89 and student_scores[scores]>79:
        student_grades[scores]= "Good"
    elif student_scores[scores]<=79 and student_scores[scores]>69:
        student_grades[scores]= "Average"
    elif student_scores[scores]<=69 and student_scores[scores]>59:
        student_grades[scores]= "Below Average"
    
print(student_grades)

