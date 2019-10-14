# slicing a specific data from a list with starting index included and ending index
# execluded

friends = ["Tuka", "Lara", "kane", "Baron", "Ralph"]
# below line will print a slice of the list starting from index 2 and ending at 4
print(friends[2:4])
# output: ['kane', 'Baron']

# list[x:]/list[:x] slice from index x to the last/first element of the list
print(friends[1:]) # output: ['Lara', 'kane', 'Baron', 'Ralph']

print(friends[:4]) # output: ['Tuka', 'Lara', 'kane', 'Baron']

# negative numbers can be used for slicing as well, but it slices from the end
# in the friends list Tuka is index [0] or [-5], while Ralph is [4] or [-1]

print(friends[-1:])  # output ["Ralph"]
print(friends[-5:])  # output ['Tuka', 'Lara', 'kane', 'Baron', 'Ralph']
print(friends[-3:4]) # output ['kane', 'Baron']
print(friends[-1:0]) # output [], slicing must be left-right.
print(friends[-1:-5]) # output [], slicing must be left-right.

# strings can be sliced as well using same way:
a_string = "United States of America"

print(a_string[0:6]) #output United
print(a_string[-2:]) # output: ca
