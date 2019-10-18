# in python functions are first class functions, acting the same way as integer and
# string would act when assigned to a variable or passed to another function as
# argument.

# example for first class function acting like variable
def greet():
    print("Hello")

# as we know from before, to execute the function we need to add () afeter the
# function name:
greet()

# putting only the name of the function without executing it with () will make
# the name like a variable containing the function:
greet
print(greet)
print(type(greet))  # output <class 'function'>

# assigning the function name to avariable, make this function value for the new var

hello = greet

print(hello)
# and it can be executed as well
hello()  # output Hello

print("=============================================")

# function as an argument to another function:
def before_after_func(func):
    print("Before...")
    func()
    print("After...")

before_after_func(greet)

# the above are two examples of first class function preperty of python

# let's experiment little bit

def names():
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")

    return f_name, l_name

def first_class(func):
    execute = func()
    print(f"{execute[0]} {execute[1]}")
    print(type(execute))

first_class(names)
