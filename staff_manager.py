class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


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
