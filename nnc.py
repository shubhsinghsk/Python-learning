# Example of class inheritance and class variables
class Course:
    # Class variable shared by all instances
    course = "Python"

class Student(Course):
    # Class variable overriding parent's
    course = "SQL"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
        # Changing class variable's value
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)

# Creating object of Student class
stud = Student("Emma")
s2 = Course()
stud.show_student()
print(s2.course)

# Parent class course name
print('Parent Class Course Name:', Course.course)