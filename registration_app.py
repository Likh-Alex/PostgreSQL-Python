def create_student():
    #Ask user for the student name and marks
    student_name = input("Enter your name: ")
    # create a dict in the format {'name':student_name, 'marks': []}
    student = {'name':student_name,
               'marks': []}
    # return the dictionary
    return student

def add_marks(student, mark):
    student["marks"].append(mark)

def calc_avg_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0
    total = sum(student['marks'])
    return total/number

new_student = create_student()