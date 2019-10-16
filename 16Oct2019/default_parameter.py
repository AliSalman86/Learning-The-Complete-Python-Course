# by assigning a valie to a function parameter, this value would be used as default in case the
# function called without a value assigned for that parameter
# this called default parameter, parameter declared while defined
def add (x, y = 3):
    total = x + y
    return total

# below function will use 12 as a value passed for parameter y
print(add(5, 12))
# below the default value of y, 3, will be used.
print(add(4))

# different from default parameter we have named arguments as below, it's used when function used
print(add(x = 5, y = 9))
print(add(4, y = 96))

# below call will return error because all arguments follow named arguement need to be named as well.
# print(add(x = 55, 5)), same applicable for default params as well

# argument without name is called positioned argument
# argument with name is keyword argument

# sep argument, sets a separater between arguments.
print(1,2,3,4,5)
print(1,2,3,4,5, sep = ", ")

# below is discouraged, as if the variable value changes, that won't reflect on the function

default_y = 7

def multiply(x, y = default_y):
    multiplied = x * y
    return multiplied

print(multiply(2))

default_y = 5
# below will be 14 as well as the function still use default_y = 7 even after being changed in the
# global body.
print(multiply(2))
