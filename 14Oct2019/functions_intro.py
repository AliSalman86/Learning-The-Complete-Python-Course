# all functions in python start with def, built in function to create a function

def greeting():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
# function only can be executed after it been declared with def
# variables created inside a function like name variable above is a local function
# to the function greeting, and can't be printed or used out of this function or in
# the global environment
greeting()

# variable scope: local or global
# in nested functions the inner function has an access to the variables
# declared in the parent evironment, other function or global.
f_name = input("Enter first name: ")
def input_name():
    l_name = input("Enter last name: ")
    def print_name():
        # notice that the print_name function has an access to the f_name declared in
        # the global scope and to the l_name declared in the parent function.
        print(f_name + " " + l_name)
    print_name()

input_name()
