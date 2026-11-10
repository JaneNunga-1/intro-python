# bank
import datetime


class Client:
    def __init__(self, name, kra_pin, gender, dob):
        self.name = name
        self.kra_pin = kra_pin
        self.gender = gender
        self.dob = dob
    def calc_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.dob, "%d-%m-%Y")
        age=today.year-birth_date.year
        return age

    def show_details(self):
        print(self.name)
        print(self.kra_pin)
        print(self.gender)


class BankAccount:
    def __init__(self, owner, balance, acc_no):
        self.owner = owner
        self.balance = balance
        self.acc_no = acc_no

    def deposit(self, amount):
        # THIS MEANS THAT THE AMOUNT WHEN U DEPOSIT ITS GOING TO INCREASE THE BALANCE
        # the absolute function makes sure it is a + value
        self.balance += abs(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def show_details(self):
        print(self.owner.name)
        print(self.acc_no)
        print( self.balance)

# since we have so many classes we need to specify from which class are we creating the object from
# when u print functions u add the () but the variables no brackets

jane=Client("Jane","A-0980","Female","06-09-2005")
ahmed=Client("Ahmed","a-987682","Male","20-11-1990")

a1=BankAccount(jane,2000000,"199282890")
a2= BankAccount(ahmed,20000000,"990289890")

a1.deposit(90000)
a1.withdraw(100000)
a1.show_details()


a2.deposit(100000)
a2.withdraw(100000)
a2.show_details()

dob='06-09-2005'
print(jane.calc_age())




