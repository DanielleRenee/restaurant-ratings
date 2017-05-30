"""Restaurant rating lister."""

restaurant_ratings = {}

print("\n")
print("CURRENT RESTAURANT RATINGS")
print("\n")

def read_file(filename):

    f = open(filename)
    for line in f:
        line = line.strip()
        line = line.split(":")
        restaurant_ratings[line[0]] = line[1]
    return restaurant_ratings

#print read_file("scores.txt")

def add_restaurant_rating(restaurants):

    new_restaurant = raw_input("Would you like to add a new restaurant? " + 
    "Please enter the name of a restaurant you would like to add? -->  ")   

    print("\n")

    new_rating = int(raw_input("Please enter the restaurant's score. -->  "))

    print("\n")

    restaurants[new_restaurant] = new_rating

    return restaurants

restaurant_ratings = read_file('scores.txt')

restaurant_ratings = add_restaurant_rating(restaurant_ratings)

# print restaurant_ratings

def sort(restaurant_ratings):

    restaurant_ratings.items()
    sorted_restaurant = sorted(restaurant_ratings.items())
 
    return sorted_restaurant
# print("\n")

def print_rest(sorted_restaurant):
    
    for restaurant, rating in sorted_restaurant:
        print "{} is rated at {}.".format(restaurant, rating)



# print("\n")

# print restaurant_ratings

    # answer = raw_input("Do you want to add a restaurant? Y/N")

#print sorted_restaurant

# restaurant_ratings = {}

# print("\n")
# print("CURRENT RESTAURANT RATINGS")
# print("\n")

# f = open("scores.txt")
# for line in f:
#     line = line.strip()
#     line = line.split(":")

#     restaurant_ratings[line[0]] = line[1]
#     restaurant_ratings.items()
#     sorted_restaurant = sorted(restaurant_ratings.items())

# for restaurant, rating in sorted_restaurant:
#     print "{} is rated at {}.".format(restaurant, rating)

# print("\n")

# new_restaurant = raw_input("Would you like to add a new restaurant? " + 
# "Please enter the name of a restaurant you would like to add? -->  ")   

# print("\n")

# new_rating = int(raw_input("Please enter the restaurant's score. -->  "))

# restaurant_ratings[new_restaurant] = new_rating

# print("\n")

# print restaurant_ratings