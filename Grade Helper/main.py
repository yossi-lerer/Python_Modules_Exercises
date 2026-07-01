from grade_app import run_grade_helper
from grade_data import get_students

def main():
    print("\n=========================================================================================")
    run_grade_helper(get_students())
    print("\n=========================================================================================")

main()
