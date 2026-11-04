#classes
class Person:
    # constructor
    def __init__(self, name,dob, age,height,weight):
     self.name = name
     self.age = age
     self.dob = dob
     self.height = height
     self.weight = weight

    def get_bmi(self):
       bmi=self.height/(self.weight)**2
       return bmi
    def show_details(self):
        print(f"My name is {self.name} born on {self.dob} and I am {self.age} years old.I am {self.height} and i weigh {self.weight} and my bmi is {round(self.get_bmi(),2)} ")

# creating an object the syntax is : objectname=classname(values as per the arguments)
p1 =( Person("Jane","06-09-2005",21,21,98) )
p1.show_details()


# for duplicating a code of line ctrl+d


p2 =Person("Margaret","29-10-2007",19,15,45 )
p2.show_details()
p2.get_bmi()
