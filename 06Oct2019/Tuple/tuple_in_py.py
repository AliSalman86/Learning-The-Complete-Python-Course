# Tuples are similar to list
# no square brakets when defining Tuples
# may use () to clear the data isinstance

short_tuple = "Ralph", "Bob"
more_clear_tuple = ("Ralph", "Bob")

print(type(short_tuple))
print(type(more_clear_tuple))
# when we need to include a tuple in a list we need to use () or Python whould thing
# the tuple is a 2 strings in the list

wrong_tuple_in_list = ["Ralph1", "Bob1"]
print(f"Type of the first object in the list is: {type(wrong_tuple_in_list[0])}.")

tuple_in_list = [("Ralph2", "Bob2")]
print(f"Type of the first object in the list is: {type(tuple_in_list[0])}.")


not_tuple_example = "Rapo"
tuple_example = "Rapo", "", ""
print(f"Type of not_tuple_example is: {type(not_tuple_example)}.")
print(f"Type of tuple_example is: {type(tuple_example)}.")

# no append() for tuples, instead we use below to add a new element to a tuple

longer_tuple = short_tuple + ("Alex",)

print(longer_tuple)
print(f"Type of longer_tuple is: {type(longer_tuple)}.")

longer_tuple = longer_tuple + ("Sara",)
print(longer_tuple)
