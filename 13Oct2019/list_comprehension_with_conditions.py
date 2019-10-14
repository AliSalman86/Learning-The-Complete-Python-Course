# we can use conditions with list comprehension to make it more flexible.
# Info: we have 2 lists, a list of friend names and a list of event's guest names
# Problem: we want to find list of friends who attended the party.
# there is to solutions:

# Solution 1: using sets and intersection() without list comprehension,
# valid but longer solution:

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# for accurate comparison we need to turn all names to all lower case letters,
# to avoid the issue of having a name in title case in one list and in lower case
# in the other list
# convert the new lists to sets:

friends_lower = set([friend.lower() for friend in friends])
guests_lower = set([guest.lower() for guest in guests])

# print unique values, guests who are friends, using sets and intersection() and
# convert the set to list so we can make the names title case using title()
present_friends = list(friends_lower.intersection(guests_lower))
present_friends_proper = list()

for name in present_friends:
    present_friends_proper.append(name.title())

print(present_friends_proper)

# solution 2: using list comprehension with conditionals

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# convert the two lists to all lower case for valid comarison
friends_lower2 = [friend.lower() for friend in friends]
guests_lower2 = [guest.lower() for guest in guests]

# print(friends_lower2)
# print(guests_lower2)

present_friends2 = [
    # select a name from the friends list
    name.title() for name in friends_lower2
    # if the friend name is in the guests list as well
    if name in guests_lower2
]

print(present_friends2)
