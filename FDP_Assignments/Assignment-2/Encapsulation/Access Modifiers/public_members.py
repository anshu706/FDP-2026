class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)


emp = Employee("Jayesh")
emp.display_name()   # Accessible
print(emp.name)      # Accessible
