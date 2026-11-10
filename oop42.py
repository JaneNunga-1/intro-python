#inheritance
class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def show_details(self):
        print(self.name,self.salary,self.department)
class Permanent_Employee(Employee):
    def __init__(self,name,salary,department,cover,increment):
        super().__init__(name,salary,department)
        self.name=name
        self.salary=salary
        self.department=department
        self.cover=cover
class ContractEmployee(Employee):
    def __init__(self,name,salary,department,tenure):
        super().__init__(name,salary,department,)
        self.name=name
        self.salary=salary
        self.department=department
        self.tenure=tenure
        #overriding


