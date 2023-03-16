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

# FROM THE TERMINAL, READ WHICH INFORMATION IS REQUIRED
if len(sys.argv) > 1:
    if sys.argv[1] in ('1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d'):
        for person in journal:
            if person.designation == 'nauczyciel':
                pass
            else:
                if person.classroom == sys.argv[1] or sys.argv[1] in person.classroom:
                    print(person.designation, ' : ', person.name)
    hisClasses = []
    for person in journal:
        if person.name == sys.argv[1] and person.designation == 'wychowawca':
            hisClasses = person.classroom
            print(person.designation, ' : ', person.name)
        if person.designation == 'uczen' and person.classroom in hisClasses:
            print(person.name, ' : ', person.classroom)
    for person in journal:
        if person.name == sys.argv[1] and person.designation == 'nauczyciel':
            hisClasses = person.classroom
        for person in journal:
            if person.designation == 'wychowawca':
                for i in person.classroom:
                    headTeachers = []
                    if i in hisClasses and person.name not in headTeachers:
                        headTeachers.append(person.name)
    if len(headTeachers) > 0:
        print(headTeachers)
    for person in journal:
        if person.name == sys.argv[1]:
            currentClass = person.classroom
    for person in journal:
        if person.designation == 'nauczyciel' and currentClass in person.classroom:
            print(person.name, ' : ', person.subject)

