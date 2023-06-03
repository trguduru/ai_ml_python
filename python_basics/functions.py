# examples for using functions
# A function can accept various data types and do some processing
# the above are built in functions in the python libraries

print(type(False))

names = ["Ram", "Bheem", "Krishna"]
ages = [10, 9, 11, 25]  # the last value will be omitted as it didnt matched with the above names list

list_of_students = list(zip(names, ages))

print(list_of_students)


#  Here is an example of creating a user defined function
def add(x, y):
    """Adds two number"""  # this is how you can add function documentation
    return x+y


def say_hello(name):
    if len(name) > 0:
        print("Hello, " + name)
    else:
        print("Hello, World !!!")


print(add(2, 3))
say_hello("Reddy")
say_hello("")
say_hello(name="John")  # you can provide a parameter name when calling the function


def student_grades(score):
    """Grades students based on the score"""
    if score >= 70:
        print("A++")
    elif 60 < score < 70:
        print("A")
    else:
        print("B")


print(student_grades(50))



