class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def role(self):
        print(self.name, "works as an employee")


class Intern(Person):
    def role(self):
        print(self.name, "is an intern")


emp = Employee("Amit")
emp.role()

intern = Intern("Shlok")
intern.role()
