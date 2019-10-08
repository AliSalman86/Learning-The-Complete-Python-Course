# you can input any letter but it will actually do something only if p entered to
# print hello or entered q to quit the program

user_input = input("Please input your choice p to start the prgram or q to terminate: ")


# Then, begin a while loop that runs for as long as the user doesn't type 'q', if q
# entered then program terminate.
while user_input != "q":
# if user input p then hello printed
    if user_input == "p":
        print("Hello!")
# ask user again what to input p to print again or q to quit
# entering any other letters would led the program to input a letter again without
# printing or quiting
    user_input = input("Please input your choice p to start the prgram or q to terminate: ")
print("program terminated")
