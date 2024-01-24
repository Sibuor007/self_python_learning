student_marks = {
    "Jenny": 92,
    "Harry": 78,
    "Dimpy": 56,
    "Rahul": 41,
    "Aniket": 99,
    "Prem": 34
}
student_grade = {} # create an empty dictionary
for item in student_marks:  # item will only hold keys
    marks = student_marks[item] # extract the values for each key in every iteration
    # the check for conditions as per grading system
    if marks > 90:
        student_grade[item] = "A+"
    elif marks > 80:
        student_grade[item] = "A"
    elif marks > 70:
        student_grade[item] = "B+"
    elif marks > 60:
        student_grade[item] = "B"
    elif marks > 50:
        student_grade[item] = "C"
    elif marks > 40:
        student_grade[item] = "D"
    else:
        student_grade[item] = "F"
# print the new created dictionary with keys and grades
print(student_grade)
