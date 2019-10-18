# lambda functions get inputs, do a small amount of processing then return outputs
# functions can do 2 things:
# 1- perform an action (not a lambda function):
print("I am a function that perform an action, showing people a print, without changing the data")

# 2- return an output(can be used as lambda function):
def divide(x, y):
    return x / y

# to turn the above divide function to a lambda function, we can do below
# variable = lambda keyword list of params(inputs): the processing(outputs)
l_divide = lambda w, z: w/z

print(divide(6, 3))

# lambda functions can be self triggered or executed:
print((lambda x, y: x / y)(15, 3))

print("===============================================================")
# lambda usage:
# non-lambda:

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]


def average(sequence):
    return sum(sequence) / len(sequence)
for student in students:
    print(f"{student['name']} has an average grades of: {average(student['grades'])}")


print("===============================================================")
# lambda usage:
# lambda:

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]


average_1 = lambda sequence: sum(sequence) / len(sequence)


for student in students:
    print(f"{student['name']} has an average grades of: {average(student['grades'])}")
