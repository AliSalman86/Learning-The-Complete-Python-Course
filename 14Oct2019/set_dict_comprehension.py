# just similar to list comprehension we can have set comprehension

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# instead of [] we can use {} for set comprehension, that would create set directly
# instead of using set()
friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}

print(present_friends)

# Dictionary comprehension is possible as well by paring keys and values from multiple
# lists with utilizing the Index

apps = ["Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter", "Udacity", "Udemy", "Pandora"]
ratings = [4.3, 4.5, 3.9, 3.4, 3.5, 4.8, 4.9, 2.7]

lower_rating = float(input("Please input the lower limit of the app rating: "))
upper_rating = float(input("Please input the upper limit of the app rating: "))

results = {
    apps[i]: ratings[i]
    for i in range(len(apps))
    if ratings[i] >= lower_rating and ratings[i] <= upper_rating
}

for app, rating in results.items():
    print(f"{app} has {rating} in the app store")
