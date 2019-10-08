# loops in python useful to repeat something for number of times.
# also evaluate argument to true or false, to execute the indented block or loop body
# two types of loops in python: for and while
# while loop is to repeat something undefined number of times till the user stop it
# for loop on other hand run the loop for a specific range or number of times.
# beware of your loop not to be infinite Loop

# while loop:
is_learning = True
# below loop will keep running till is_learning changed to false
while is_learning:
    # print("You are learning")
    # is_learning = False
    # better way to validate if the loop statement still valid
    # loop will stop only if empty string input
    # if you put no, False or 0 it will continue looping
    # is_learning = input("Are you still learning: ")
    # one weak fix to the above statement is:
    user_input = input("Are you still learning?")

    is_learning = user_input == "yes"

# Program launcher using while Loop

user_input = input("Do you wish to start running the program? (yes/no): ")
counter = 0
while user_input in ["yes", "1", "true", "ok", "sure", "continue", "yeah", "yep"]:
    counter += 1
    print("========================================")
    print(f"Program is running for {counter}")
    print("========================================")
    user_input = input("Do you wish to continue running the program? (yes/no): ")

print("You exited the program")
