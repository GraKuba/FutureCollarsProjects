import sys

# MAIN CLASS FOR CREATING DESIGNATED OBJECTS - HEADTEACHER, TEACHERS AND STUDENT
class School:
    def __init__(self, designation, name, classroom, subject = None): 
        self.designation = designation
        self.name = name
        self.classroom = classroom
        self.subject = subject 


# CREATING OBJECTS, USING DATA FROM IN.TXT
journal = []
while True:
    designation = input()
    if designation == 'wychowawca':
        name = input()
        classes = []
        while True:
            classrooms = input()
            if classrooms == '':
                break
            else:
                classes.append(classrooms)
        headTeacher = School('wychowawca', name, classes)
        journal.append(headTeacher)
    elif designation == 'nauczyciel':
        name = input()
        subject = input()
        classes = []
        while True:
            classrooms = input()
            if classrooms == '':
                break
            else:
                classes.append(classrooms)
        teacher = School('nauczyciel', name, classes, subject) 
        journal.append(teacher)
    elif designation == 'uczen':
        student = School('uczen', input(), input())
        journal.append(student)
    elif designation == 'koniec':
        break

for person in journal:
    print(person.designation, " : ", person.classroom)

# FROM THE TERMINAL, READ WHICH INFORMATION IS REQUIRED
if len(sys.argv) > 1:
    pass
