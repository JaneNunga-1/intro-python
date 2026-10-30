from codecs import namereplace_errors
from datetime import date, datetime


# creating a class
class Client:
    def __init__(self, name, kra_pin, dob, gender):
        self.name = name
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.name)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%d-%m-%Y")
        age = today.year - birth_date.year
        return age


class BankAccount:
    def __init__(self, owner, acc_no, balance):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.name)
        print(self.acc_no)
        print(self.balance)
        print("---------------")


jane = Client(name="Jane Nunga", kra_pin="A09", dob="06-09-2005", gender="F")
ahmed= Client(name="Ahmed Muhammed", kra_pin="A0999", dob="20-09-1980", gender="M")
account1 = BankAccount(jane, "123", 100)
account2 = BankAccount(jane, "183", 50000)
account3 = BankAccount(jane, "156", 107770)

account1.deposit = (30000)
account2.deposit = (70000)

account1.print_details()
account2.withdraw = (2400)
account2.print_details()
print("Jane age is", jane.calc_age())
print(account1.owner.calc_age())
print("Ahmed is ", ahmed.calc_age(),"years old")
