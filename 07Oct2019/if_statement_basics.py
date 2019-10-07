# if statement is logical statement help a program taking decision using boolean
# if statement structure is:
# if True:
#     code block to be executed
# the spaces left before the executable code is on purpose as python use the indenting
# to recognise the code belongs to specific if statement
# ==========================================
# if true:
#     first if statement Block
#     if true:
#         second if statement block
#     continuation of firt if statement
# Continuation of the main Code
# ==========================================
# else statement related to if statement need to come directly below it, no general
# code between the if and else

friend = "Ralph"
user_name = input("Enter your name: ")

# if True
if user_name == friend:
    print("Hello " + user_name)
# else if False
else:
    print("Wrong user name, {name}".format(name = user_name))
# below will run anyway since it's outside the if statement
print("What you want to do today?")

# if block will only executed if the statement evaluate to True

your_name = input("Please enter your name: ")

# if you don't enter a name then the if statement will evaluate to false. returning
# nothing
if your_name:
    print(f"Welcome back {your_name}")

# "in" keyword with if statement
# below code print hello friend if the entered name belong to the friends list, prints
# hello family if entered name matches a family name in the family list, and print
# I don't know you if matches no name in neither of the lists

friends_list = ["Alex", "Karen", "Morgan", "John"]
family_list = ["Adam", "Carl", "Mona", "Jenna"]

user_name = input("Please enter a name: ")
if user_name in friends_list:
    print(f"Hello firend, {user_name}")
elif user_name in family_list:
    print(f"Hello family, {user_name}")
else:
    print(f"I don't know you, {user_name}")
