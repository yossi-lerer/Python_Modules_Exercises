def get_grade_status(grade):
    if grade >= 90:
        return "Excellent"
    elif grade >= 60:
        return "Passed"
    elif grade < 60:
        return "Failed"

def calculate_average(total_grades, students):
    return total_grades / students