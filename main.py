import sys

# CLASSES FOR THREE MAIN OBJECTS
class HeadTeacher:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom


class Teacher:
    def __init__(self, name, classroom, subject):
        self.name = name
        self.classroom = classroom
        self.subject = subject


class Student: 
    def __init__(self, name, classroom):
        self.name = name 
        self.classroom = classroom 



# FROM THE TERMINAL, READ WHICH INFORMATION IS REQUIRED
if len(sys.argv) > 1:
    pass