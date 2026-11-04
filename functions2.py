def add(a, b, c):
    s = a + b + c
    return s


print(add(2, 4, 8))


def addition(x, *args):
    #documentation of a function
    """
    adds numbers as per the stated arguments
    param x is integer
    returns sum  in integers
    """
    total = x * (sum(args))
    return total


print(addition(2, 2, 3, 4, 78, 90))


def build_profile(
        **kwargs):  # this is a function that creates a  dictionary which accepts a key and a value for the key  key-word arguments
    for k, w in kwargs.items():
        return k, w


print(build_profile(occupation="CEO", name="Jane", age="21", company="NungaCreatives"))

# anonymous functions==lambda
# lambda function means u  dont need to write the normal way of writing the functions like the word def and all that
# normal way of writing a function: def square(number):
#     return number*number
# print (square(5))
# using lambda
square = lambda x: x ** 2  # this means x is the value and it will be squared
# return in lamda is used when u have specified ur own expressions like x*m something like that

print(square(5))

people = [
    {"name": "Brian", "age": 21},
    {f"name": "Pane", "age": 21},
    {f"name": "John", "age": 34},
    {f"name": "Mary", "age": 89},
]
# lamda can be used to sort out items
sorted_age = sorted(people, key=lambda x: x["name"],reverse=True)
print(sorted_age)
