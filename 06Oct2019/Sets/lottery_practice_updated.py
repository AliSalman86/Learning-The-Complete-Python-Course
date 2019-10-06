# this is an update or rev1 for the lottery practice, as I found out that we can use set() to create a set instead of initiating it with empty set with
# {""}, that would save us from adding initial line to remove the empty "", previous code is still there but commented out

# this practice is to compare the winning lottery numbers to the tickets the user have
# the user to input his ticket numbers, stored as a set and compare it to the wining numbers
# for now this only use sets and no conditional statements, and the project to be updated as the learnning continue

# hard coding the winning numbers of the week

winning_ticket = {"32", "24", "8", "41", "4", "52", "42"}
# ***needed to add "" inside the {} other wise the data type would be dictionary instead of set***
# updated, the easier way to initiate a set is to use set()
# user_numbers = {""}
user_numbers = set()
print(type(user_numbers)) # for debugging

# user inputs the ticket numbers

user_numbers.add(input("Enter the 1st number: "))
user_numbers.add(input("Enter the 2nd number: "))
user_numbers.add(input("Enter the 3rd number: "))
user_numbers.add(input("Enter the 4th number: "))
user_numbers.add(input("Enter the 5th number: "))
user_numbers.add(input("Enter the 6th number: "))
user_numbers.add(input("Enter the 7st number: "))
# user_numbers.remove("")   # to remove the empty "" added for the set type during the initiation

# print(user_numbers)

matched_numbers = winning_ticket.intersection(user_numbers)
# print(matched_numbers)  #for logs
matched_count = matched_numbers.__len__()

# simple way to state money gained depend on fixed amount of money per correct number

money_gained = matched_count * 100

# print(matched_count)    #for logs

# give the answer to the user about how many numbers he have matching the wining ticket
# and what is the matched matched numbers

print(f"You have {matched_count} matched numbers and they are: {matched_numbers}, you won ${money_gained}, Congrats!")

# problems in this code is that
# 1- winning ticket numbers are hard coded, will be better to be interactive
# 2- there is no way to state how much user won based on how many tickets he matched
# 3- no way in sets to hold an order so no clear way to declare a power ball or number
