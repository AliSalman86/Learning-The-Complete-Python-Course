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
# practice for comprehension
names = ["Alex", "Alice", "Jaafar", "Jenna"]
last_name = "Jordan"

full_names = [f"{name} full name is {name} {last_name}." for name in names]

print(full_names)

print("=========================================")
# multi lists comprehension

a_numbers = [3, 4, 5, 6]
b_numbers = [8, 5, 3, 1]

multiplied = [a * b for a in a_numbers for b in b_numbers]

print(multiplied)
print(f"multiply a_numbers list by b_numbers list give us {len(multiplied)} possibility")

print("=========================================")

# validating names to true is first letter is capital or small
# lower(), will make all letters in a string in a list lower case.
# title(), make every string in a list start with capital letter.

friend = input("Enter your name: ")
friends = ["Alex", "Alice", "Jaafar", "Jenna"]
friends_lower = [name.lower() for name in friends]
print(friend)
print(friends_lower)

if friend.lower() in friends_lower:
    print(f"Hello {friend.title()}")
else:
    print(f"Hi, nice to meet you {friend.title()}")
