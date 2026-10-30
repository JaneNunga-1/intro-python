from operator import truediv


def greet():
    print("Hello World")


greet()  # use ur function by calling it


# the function greet doesnt have data or parameters
def take(name):
    print(f"Take this{name}")


def volume_cylinder(height, radius):
    v = 22 / 7 * radius ** 2 * height


def volume_cylinder_better(height, radius):
    vb = 22 / 7 * radius ** 2 * height
    a = 2 * 22 / 7 * radius ** 2 * height
    # we need to like store the function in a va\riable but it wont print it out by using the return function
    return vb, a


# we have store the result i a variable called result
vb, a =volume_cylinder_better (height=20,radius=3)
print(f"volume is {round(vb,2)} and area is {round(a,2)}")

def divide(a,b,should_round=False):
   res=a/b
   if should_round == True:
       return round(res,2)
   else:
       return res
print(divide(20,2,True))
