# sets like lists and tuples is a collection of data, with the below differences
# sets does not hold order
# does not contain duplicate values
# sets can be initiated by using {}

art_friends = {"Anna", "Chris"}
science_friends = {"Jen", "Tuka"}
print(f"The type of art_friends data is: {type(art_friends)}")

# add() attribute can be used to add a new element to anywhere in the set (No order)
art_friends.add("Amanda")
print(art_friends)

# result is {'Amanda', 'Chris', 'Anna'}, notice Amanda was added as the first element

# print(art_friends[0])

# running the above command to search for value associated to an index return an
# error TypeError: 'set' object is not subscriptable, since sets hold no position or
# order, so no indexing

# remove() can be used to remove an element by specifing the exact name of the element

art_friends.remove("Amanda")
print(art_friends)

# Advanced set operations
# One of the best uses of sets is that it's easy to compare two sets to:
# find common elements between 2 sets or find elements that in one set but not
# in the other set
