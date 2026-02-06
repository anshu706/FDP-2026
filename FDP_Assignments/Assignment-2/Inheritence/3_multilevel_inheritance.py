class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def show_role(self):
        print(self.name, "is an employee")


class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages", dept, "department")


mgr = Manager("Dinesh")
mgr.show_role()
mgr.department("HR")
