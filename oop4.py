#inheritance
class Employee:
    def __init__(self,name,email,department,salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
    def show_details(self):
        print(self.name,self.salary)
class Permanent(Employee):
    def __init__(self,name,email,department,salary,cover,increment):
        super().__init__( name, email,department,salary)
        self.cover = cover
        self.increment = increment
class Contractor(Employee):
    def __init__(self,name,email,department,salary,tenure):
        super().__init__(name,email,department,salary)
        self.tenure = tenure
p1=Permanent("Jane","nungalegal@gmail.com""","IT","1000002","1000000","10000")
c1=Contractor("Jane","nuhyss@hhjshsn","fINACE","89099009","10009999",)
p1.show_details()
c1.show_details()