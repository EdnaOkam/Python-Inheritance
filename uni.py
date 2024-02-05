class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age 

    def display_info(self):
        print(f"Name: {self.name} \n Age: {self.age}")

class Student(Person):
    def __init__ (name, age, student_id, courses, assignments_due=0 ):
        super().__init__( name, age)
        self.student_id = student_id
        self.courses = []
        self.assignments_due = assignments_due = 0 

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id} \nCourses taken {[self.courses]} \nAssignments Due: {self.assignments_due}")

    def submit_assignment(assignment_name):
        assignment_name = self.assignments_due
        print(f"Student {self.name} submitted assignment : {assignment_name}")

    def attend_class(self):
        self.student_id = self.courses
        print(f"Student {self.name} attends {self.courses} classes.")

class Teacher(Person):
    def __init__ (name, age, employee_id, courses_taught, office_hours ):
        super(). __init__ (name, age)
        self.employee_id = employee_id
        self.courses_taught = []
        self.office_hours = {}

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id} \nCourses Taught: {self.courses_taught} \nOffice Hours: {self.office_hours}")

    def schedule_office_hours(day,time):
        print(f"Scheduled Office Hours for Employee ID : {self.employee_id} : {days} at {time}")

student1 = Student("Ezra" , 18, "23456", ["Physics", "Math", "Biology"])
student1.display_info()
student1.assignments_due(4)
student1.submit_assignment("Physics Assignment 1")
student1.attend_class()

teacher1 = Teacher("Mr. David", 34," 45623", ["Physic", "Math"] )
teacher1.schedule_office_hours("Monday" "Wednesday", "9:00 AM - 11:00 AM", "1:00 PM - 2:00 PM ")
teacher1.display_info()


    


