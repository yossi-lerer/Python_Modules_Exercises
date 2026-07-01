def print_student_result(name, grade, status):
    print(name, grade, status)
def print_skipped_student(error, student):
    list_err = []
    for i in error:
        if i != True and i != False:
            list_err.append(i)
            # print(f"Skipped student: {i}")
    error_i = 1
    if list_err != []:
        print(f"\nSkipped student: {student}")
        for i in list_err:
            print(f"{error_i}. {i}")
            error_i += 1
def print_summary(average, passed_count):
    print(f"\naverage: {average}, passed student: {passed_count}")
