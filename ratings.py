"""Restaurant rating lister."""

restaurant_ratings = {}

f = open("scores.txt")
for line in f:
    line = line.strip()
    line = line.split(":")

    restaurant_ratings[line[0]] = line[1]
    restaurant_ratings.items()
    sorted_restaurant = sorted(restaurant_ratings.items())

for restaurant, rating in sorted_restaurant:
    print "{} is rated at {}.".format(restaurant, rating)

#print sorted_restaurant
