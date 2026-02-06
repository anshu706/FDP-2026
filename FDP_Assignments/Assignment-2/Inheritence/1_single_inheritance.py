class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")


emp = Employee("Robin")
print("Name:", emp.name)
emp.show_role()
