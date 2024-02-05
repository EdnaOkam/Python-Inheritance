class Employee:
    def __init__ (self, name, age, employee_id, salary, vacation_days=20):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.salary = salary
        self.vacation_days = vacation_days

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Vacation Days: {self.vacation_days}")

    def calculate_bonus(self):
        bonus= self.salary * 0.1
        print(f"Salary Bonus: {bonus}")
        return bonus

    def take_vacation(self,days):
        if days<= self.vacation_days:
            self.vacation_days -= days
            print(f"{self.employee_id} took {days} vacation days. Remaining vacation days left: {self.vacation_days}")
        else:
            print("You have exceeded your available vacation days.")

    def evaluate_performance(self,grade):
        print(f"Performance Evaluation Grade for {self.name} : {grade}")

class Manager(Employee):
    def __init__ (self, name, age, employee_id, salary, vacation_days=20, team_size=10):
        super().__init__(name, age, employee_id, salary, vacation_days=20)
        self.team_size = team_size

    def conduct_meeting(self):
        print(f"Manager {self.name} is conducting a meeting for {self.team_size} members.")

class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, vacation_days=20, programming_language="Python"):
        super().__init__(name, age, employee_id, salary, vacation_days=20)
        self.programming_language = programming_language

    def write_code(self):
        print(f"Developer {self.name} is writing a code in {self.programming_language}.")

employee1 = Employee("Matthew Doha", 28, 19543, 80000)
employee1.display_info()
employee1.calculate_bonus()
employee1.take_vacation(3)
employee1.evaluate_performance("Great")

manager1 = Manager("Emily Paris", 40, 12754, 120000, team_size = 10)
manager1.display_info()
manager1.calculate_bonus()
manager1.take_vacation(5)
manager1.conduct_meeting()

developer1 = Developer("Chris Brown", 30, 18843, 90000, programming_language = "python")
developer1.display_info()
developer1.calculate_bonus()
developer1.take_vacation(7)
developer1.write_code()

    