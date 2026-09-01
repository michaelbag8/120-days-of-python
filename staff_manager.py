#Inheritance in OOP
#Person
#   |
#Employee(Person)
#    |
#Teacher(Employee)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"My name is {self.name}")


class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary


class Teacher(Employee):

    def __init__(self, name, age, employee_id, salary, subject):
        super().__init__(name, age, employee_id, salary)
        self.subject = subject


teacher = Teacher(
    "Michael",
    30,
    "EMP001",
    200000,
    "Python"
)

teacher.introduce()
