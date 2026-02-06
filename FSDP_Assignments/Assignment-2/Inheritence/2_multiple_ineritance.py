class Person:
    def __init__(self, name):
        self.name = name


class Job:
    def __init__(self, salary):
        self.salary = salary


class Employee(Person, Job):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)


emp = Employee("Ashok", 50000)
emp.details()
