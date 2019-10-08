# tuple of currencies
currencies = (0.8, 1.2)
# this will take every element in the tuple and put it a new variable in sequience
# below would result usd = 0.8, eur = 1.2
usd, eur = currencies
# this is destructuring syntax
print(usd)
print(eur)

# a good use of destructuring:
# list of tuples
friends = [("Ralph", 24), ("Alex", 31), ("Anne", 27), ("Jenna", 35)]
# extract name and age values of each tuple element as we iterate
for name, age in friends:
    print(f"{name} is {age} years old")
