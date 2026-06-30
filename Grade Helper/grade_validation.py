def validate_student(student):
    try:
        return isinstance(student, tuple) and (len(student) == 2) and type(student[0]) == str and type(student[1]) == int and 0 < student[1] <= 100
    except TypeError:
        return "some value it is not good"
    except ValueError:
        pass
def validate_grade(grade):
    pass
print(validate_student(("hi", 1000)))