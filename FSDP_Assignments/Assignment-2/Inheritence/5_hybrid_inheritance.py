class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def role(self):
        print(self.name, "is an employee")


class Project:
    def __init__(self, project_name):
        self.project_name = project_name


class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)


lead = TeamLead("Sanjay", "AI Development")
lead.role()
lead.details()
