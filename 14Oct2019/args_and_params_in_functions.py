# code to calculate the mpg for a car without function
car = {
  "make": "Ford",
  "model": "Fiesta",
  "mileage": 23000,
  "fuel_consumed": 460
}

# mpg = car["mileage"] / car["fuel_consumed"]
# name = f"{car['make']} {car['model']}"
# print(f"{name} consume {mpg} per galon!")

# same application but with function, but no args and params

# def mpg_calculator():
#     mpg = car["mileage"] / car["fuel_consumed"]
#     name = f"{car['make']} {car['model']}"
#     print(f"{name} consume {mpg} per galon!")

# mpg_calculator()

# same application with function(arg):
# argument: is a vlue passed to a function
# parameter: is a variable that accept a value inside the function

def mpg_calculator(a_car, intro):
    print(intro)
    mpg = int(a_car["mileage"] / a_car["fuel_consumed"])
    name = f"{a_car['make']} {a_car['model']}"
    print(f"{name} consume {mpg} per galon!")

# car dict passed as argument to the mpg_calculator function
mpg_calculator(car, "New Car")

# using list of cars arguments

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

# iterate on the cars list and execute the mpg_calculator function with a car
# passed as an argument at a time
for car in cars:
    mpg_calculator(car, "New Car Consumption Info")
