student_list = []

def create_student():
    #Ask user for the student name and marks
    student_name = input("Enter your name: ")
    # create a dict in the format {'name':student_name, 'marks': []}
    student = {'name':student_name,
               'marks': []}
    # return the dictionary
    return student

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
    for i, student in enumerate(students):
        print(f"ID : {i}")
        print(student_details(student))


def menu():
    #add a student to a student list
    #add a mark to a student
    #Print a list of students
    #Exit the application
    selection = input("Enter 'p' to print the list of all students,"
                      " 's' to add a new student,"
                      " 'm' to add marks for the student,"
                      " 'q' to exit"
                      "\nEnter your selection: ...")
    while selection != 'q':
        if selection == 'p':
            print_all_students(student_list)
            print("No students in the list")
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'm':
            student_id = int(input("Enter the student ID to a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter a new mark to be added: "))
            add_marks(student, new_mark)

        selection = input("Enter 'p' to print the list of all students,"
                      " 's' to add a new student,"
                      " 'm' to add marks for the student,"
                      " 'q' to exit"
                      "\nEnter your selection: ...")







menu()