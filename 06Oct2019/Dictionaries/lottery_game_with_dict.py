# hard coded winning numbers
lottery_numbers = {13, 21, 22, 5, 8}

# list of 2 playes in dictionaries structure to include the player name and their
# guesses numbers
players = [
        {
            "name": "AliAS",
            "numbers": {13, 49, 22, 15, 30}
        },
        {
            "name": "Tukas",
            "numbers": {3, 15, 22, 5, 8}
        }
    ]

# extracting the guessed numbers only from the list in form of set structure, so we
# can compare it with the winning numbers set using intersection()
player1_numbers = set(players[0]["numbers"])
player2_numbers = set(players[1]["numbers"])

# for debugging only
print(type(lottery_numbers))
print(type(player1_numbers))
print(type(player2_numbers))

# comparing the players numbers to the lottery set and get the matching numbers
player1_right_numbers = player1_numbers.intersection(lottery_numbers)
player2_right_numbers = player2_numbers.intersection(lottery_numbers)

# count of each player right match numbers
player1_count = len(player1_right_numbers)
player2_count = len(player2_right_numbers)

# printing results
print(players[0]["name"] + " got " + str(player1_count) + " right!")
print(players[1]["name"] + " got " + str(player2_count) + " right!")
