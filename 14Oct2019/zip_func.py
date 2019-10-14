# zip function run on multiple lists and run a zipper on the elemets of these lists
# and combine them together into one list of tuples if we use list() or dictionary
# with key:value pairs
apps = ["Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter", "Udacity", "Udemy", "Pandora"]
ratings = [4.3, 4.5, 3.9, 3.4, 3.5, 4.8, 4.9, 2.7]

# print will only show something meaningful only if we convert the zip function result
# to list() or dict()
app_rating_list = list(zip(apps, ratings))
app_rating_dict = dict(zip(apps, ratings))

print(type(app_rating_list))
print(app_rating_list)
print(type(app_rating_dict))
print(app_rating_dict)
