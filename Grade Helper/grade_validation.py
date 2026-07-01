def validate_student(student):
    validate = False
    try:
        if isinstance(student, tuple):
            validate = True
        else:
            validate = False
            return "Data must be a tuple"
    except:
        validate = False
        return validate
    
    try:
        if (len(student) == 2):
            validate = True
        else: 
            validate = False
            return validate
    except TypeError:
        validate = False
        return validate
    try:
        if type(student[0]) == str:
            validate = True
        else:
            validate = False
            return "Name must be a string"
    except TypeError:
            validate = False
            return validate
    return validate


def validate_grade(grade):
    validate = False
    if type(grade) == int:
        validate = True
    else:
        validate = False
        return "Grade must be an integer"
    if 0 < grade <= 100:
        validate = True
    else:
        validate = False
        return "Grade must be between 0 and 100"
    return validate
