# if else
import os

name = input("Enter your name: ")
age = 21
if name == "Jane":
    {
        print("Okay Yes")
    }
else:
    {
        print("No")
    }

#     input function
age = input("Enter your age")
if not age.isnumeric():
    print("Invalid")
    # terminate
    os._exit(0)

if int(age) < 18:
    {
        print(name + " " + "is a child")
    }
else:
    {
        print(name + " " + "is an adult")
    }
