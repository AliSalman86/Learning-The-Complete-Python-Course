# for loop used to repeat a block of code for defined number of times
# the for loop structure is => for 'new var' in iterable collection of data
# data can be list, set, tuple or dictionary as all of them are iterables
# iterate: repeat the process or the block of program on all the collection elements

friends_list = ["Tuka", "Lara", "kane", "Baron"]

for friend in friends_list:
    print(friend)
print("friends list completed")
print("===================================================")
for element in range(10):
    print(element)
print("===================================================")
for element in range(5,15):
    print(element)
print("===================================================")
for element in range(3,31,3):
    print(element)

students_coding_grades = [
    {"name": "Ralph", "grade": 90},
    {"name": "Jen", "grade": 85},
    {"name": "Boo", "grade": 72}
]


students_grades = [
    {"name": "Ralph", "grade": 90},
    {"name": "Jen", "grade": 85},
    {"name": "Boo", "grade": 72}
]

# iterate on every dictionary in the list and print the student name and grade
for student in students_grades:
    print(f"{student['name']} scored {student['grade']} in coding!")
