student_list = []

def create_student():
    #Ask user for the student name and marks
    student_name = input("Enter your name: ")
    # create a dict in the format {'name':student_name, 'marks': []}
    student = {'name':student_name,
               'marks': []}
    # return the dictionary
    student_list.append(student)

def add_marks(student, mark):
    #add a mark to the student dictionary
    student["marks"].append(mark)

def calc_avg_mark(student):
    #check len of students marks
    number = len(student['marks'])
    if number == 0:
        return 0
    #calculate the average
    total = sum(student['marks'])
    return total/number

def student_details(student):
    #print out the string that tells the user the info abouth the student
        print(f"The name of the student is {student['name']}, scores are {student['marks']}"
          f" and the average mark is {calc_avg_mark(student)}")

def print_all_students(students):
    # print out the string that tells the user the info abouth the student for every student in the list
    for student in student_list:
        print(student_details(student))



new_student = create_student()
student_details(new_student)