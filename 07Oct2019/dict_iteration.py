# dictionary of data
friends = {"Ralph": 24, "Alex": 31, "Anne": 27, "Jenna": 35}

# the code below would return the keys of the dictionary
for name in friends:
    print(name)
print("=============================================================")
# using values() as attribute for the dictionary would return the values.
for age in friends.values():
  print(age)
print("=============================================================")
# using items() as attribute for the dictionary would return both keys and values.
for name, age in friends.items():
  print(f"{name} is {age} years old")
