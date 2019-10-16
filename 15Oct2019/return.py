cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

# instead of using one function to calculate mpg, name and print the car info we can do it using multiple
# functions with return

def mpg_calculator(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name

# notice that this function has no return, so we can't assign it's output to variable, otherwise var will be
# None

def car_info(car):
    mpg_return = mpg_calculator(car)
    name_return = car_name(car)

    print(f"{name_return} does {mpg_return} miles per gallon")


for car in cars:
    car_info(car)
