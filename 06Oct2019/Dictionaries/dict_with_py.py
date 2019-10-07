# dictionares is a collection of data structured in key:value pairs
# dictionares use {} like sets but in the below form
# my_dict = {"key": value}

# it is mostly usful when you have a key and want to search for associated ValueError

friend_ages = {"Ralph": 24,
                "Adam": 30,
                "Anne": 27}

# search for someone age using their name as a Key
print(friend_ages["Ralph"])

# to add a new pair to the dictionary we need to access a key and put a value for it

friend_ages["Bob"] = 20
print(friend_ages)

# to store multiplr peices of information in dictionaries we can do a list or tuple of
# dictionaries as shown below

friends = (
    {"name": "Ralph Smith", "age": 24},
    {"name": "Bob William", "age": 32},
    {"name": "Anne Pun", "age": 41}
)

# or

friends_list = [
    {"name": "Ralph Smith", "age": 24},
    {"name": "Bob William", "age": 32},
    {"name": "Anne Pun", "age": 41}
]

# to search any piece of information we can search for the list or tuple index,
# then for the key of the value we looking for

print(friends[0]["name"])
print(friends_list[1]["age"])

# dict() functoin can be passed a list of tuples or list of lists and convert it to
# dictionary
print("==================================================================")
friends_list_of_tuples = [("Anna", 23), ("Ali", 32), ("Tuka", 31), ("James", 19)]
friends_dict_from_tuple = dict(friends_list_of_tuples)
print(friends_dict_from_tuple)

print("==================================================================")
friends_list_of_lists = [["Anna", 23], ["Ali", 32], ["Tuka", 31], ["James", 19]]
friends_dict_from_lists = dict(friends_list_of_lists)
print(friends_dict_from_lists)
