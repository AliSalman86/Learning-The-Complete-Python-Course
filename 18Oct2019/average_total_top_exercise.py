# for total and top tasks, sum and max are built in functions, the lambda function
# for these 2 tasks would only execute these built in functions, so we can substitute
# the lambda function with sum and max only
operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),  # another way to write it is "total": sum,
    "top": lambda seq: max(seq),    # another way to write it is "top": max,
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"student: {name}")

    operation = input(f"""What you need to know about {name} grades:
                          1- Average
                          2- Total
                          3- Top
                          Answer: """)

    print(f"{name} grades {operation} is: {operations[operation.lower()](grades)}")
