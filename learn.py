class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email 

    def display_info(self):
        print(f"Username: {self.username} \nEmail Address:{self.email}")

class Student(User):
    def __init__(self, username, email, courses_enrolled):
            super().__init__(username, email)
            self.courses_enrolled = []

    def enroll_course(self,course):
        self.courses_enrolled.append(course)
        print(f"Student {self.username} enrolled in a new course {course}.")

    def display_courses(self):
        print(f"Courses Enrolled: {self.courses_enrolled}")

class Instructor(User):
    def __init__(self, username, email, courses_taught):
        super().__init__(username, email)
        self.courses_taught = []

    def teach_course(self,course):
        self.courses_taught.append(course)
        print(f"New Course: {course}")

    def display_courses_taught(self):
        print(f"List of Courses: {self.courses_taught}")

class PremiumStudent(Student, User):
    def __init__(self, username, email, courses_enrolled, premium_access):
        super().__init__(username, email, courses_enrolled)
        self.premium_access = premium_access

    def display_info(self):
        super().display_info()
        print(f"Premium Access: {self.premium_access}")

student_info = Student("Sarah OConner", "sara9@twitter.com", "Cybersecurity")
student_info.display_info()
student_info.enroll_course("Machine Learning")
student_info.display_courses()

instructor_info = Instructor("Meridth Grey", "grey11@twitter.com", "Data Science")
instructor_info.display_info()
instructor_info.teach_course("Big Data Analytics")
instructor_info.display_courses_taught()

premium_student_access = PremiumStudent("Beauty Bob", "beaut67@twitter.com", "Health Informatics",True)
premium_student_access.display_info()
premium_student_access.enroll_course("UI/UX Design")
premium_student_access.display_courses()