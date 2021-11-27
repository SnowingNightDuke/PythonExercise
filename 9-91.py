# Grading Program

def grading_program():
    student_scores = {
    "Harry": 81, 
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
    }

    for student in student_scores:
        if student_scores[student] > 90:
            student_scores[student] = "Outstanding"
        elif student_scores[student] > 80 and student_scores[student] <= 90:
            student_scores[student] = "Exceeds Expectiations"
        elif student_scores[student] >70 and student_scores[student] <= 80:
            student_scores[student] = "Acceptable"
        elif student_scores[student] < 70:
            student_scores[student] = "Fail"
    
    print(student_scores)

grading_program()