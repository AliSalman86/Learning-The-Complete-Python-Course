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

# ===================================================================================
# Advanced set operations
# One of the best uses of sets is that it's easy to compare two sets to:
# find common elements between 2 sets or find elements that in one set but not
# in the other set

coding_friends = {"Alex", "Yuwa", "Jenna", "James"}
photography_friends = {"Alex", "Yuwa", "Donald", "Tuka"}

# sets doesn't accept repeated or duplicate elements and that make the sets comparable

# to find the people who do coding but no photography:

coding_only = coding_friends.difference(photography_friends)
print(f"Friends who do only coding are: {coding_only} ")

photography_only = photography_friends.difference(coding_friends)
print(f"Friends who do only photography are: {photography_only} ")

# also we can filter the names for people who only have 1 hobby by using
# symmetric_difference

unique_hobby = coding_friends.symmetric_difference(photography_friends)
print(f"Friends who do only one hobby are: {unique_hobby} ")

# intersection() attribute can be used to find elements exists in 2 sets
multi_skilled = coding_friends.intersection(photography_friends)
print(f"Friends who multi skilled are: {multi_skilled} ")

# to join or unite two sets without duplicates in one set, union() can be used

all_friends = coding_friends.union(photography_friends)
print(f"All friends are: {all_friends} ")

# all above operations return a set as well.

print(f"The type of returned data from union() is: {type(all_friends)}")
