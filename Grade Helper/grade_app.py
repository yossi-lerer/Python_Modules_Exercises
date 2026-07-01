from grade_validation import validate_student, validate_grade
from grade_logic import get_grade_status, calculate_average
from grade_output import print_student_result, print_skipped_student, print_summary

def run_grade_helper(students):
    average = 0
    passed_students = 0
    count_students = 0

    for i in students:
        if validate_student(i) == True and validate_grade(i[1]) == True:
            status = get_grade_status(i[1])
            print_student_result(i[0], i[1], status)
            average += i[1]
            count_students += 1
            if status != "Failed":
                passed_students += 1
                
        else:
            print_skipped_student((validate_student(i) ,validate_grade(i[1])))
    average_calc = calculate_average(average, count_students)
    print_summary(average_calc, passed_students)