import random

# function to generate 6 random numbers in range from 0 - 22
lottery_numbers = set(random.sample(range(22), 6))
# check point
print(lottery_numbers)

# given sample of players
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# dict comprehension statement to create a dictionary with name and matched numbers
# pairs to check the highest winner
matched_numbers = {
    f"{player['name']}" : len(player['numbers'].intersection(lottery_numbers))
    for player in players
}

# check point
print(matched_numbers)

# find the name of the player with most numbers matched
winner_name = max(matched_numbers, key = matched_numbers.get)
# find the count of matched numbers, the value of the key "or the name"
winner_score = matched_numbers[winner_name]
# formula to find winnings
winning_value = 100 ** winner_score

# print results
print("================================================================")
print(f"{winner_name} matched {winner_score} and won ${winning_value}")
print("================================================================")
