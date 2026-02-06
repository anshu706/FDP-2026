class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute


emp = Employee("Ramesh", 50000)
print(emp.name)
print(emp._Employee__salary)
