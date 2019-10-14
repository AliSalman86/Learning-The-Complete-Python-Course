# list comprehension is a python feature that allows us to create lists very
# succinctly but being very powerful.

# doubling a list of numbers without list comprehension:
numbers = [0, 1, 2, 3, 4, 5]
doubled_numbers = list()
# use for loop to iterate the numbers in the list and multiply it by 2

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)
print("=========================================")
# same above with list comprehension
numbers_2 = [1, 2, 3, 4, 5]
doubled_numbers_2 = [number * 2 for number in numbers_2]

print(doubled_numbers_2)

print("=========================================")
