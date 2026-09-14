# # cars = ['bow', 'audi', 'toyota', 'subaru']
# # print(cars)
# # # cars.sort(reverse=True)

# # # print("Here is the original list:")
# # # print(cars)

# # # print("\nHere is the sorted list:")
# # # print(sorted(cars))

# # # print("\nHere is the original list again:")
# # # print(sorted(reverse=True)(cars))

# # cars.reverse()
# # print(cars )

# # travel  = ['california', 'antartica', 'new orleans', 'jamaica', 'italy']
# # print(travel)
# # print(sorted(travel))
# # # print(sorted(reverse=True)(travel))
# # print(travel)
# # travel.reverse()
# # print(travel)
# # travel.reverse()
# # travel.sort()
# # print(travel)
# # travel.sort(reverse=True)
# # print(travel)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# for value in range(6):
#     print(value)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):         #First 
#      squares.append(value**2)    #Method(longer)
# print(squares)

# squares = [value**2 for value in range(1,11)]  #Second
# print(squares)                                #Method(shorter(list comprehnshions))

# for value in range(1,21):
#     print(value)

# for value in range(1,1000000):
#     print(value)

# values = list(range(1,1000001,3))
# print(values)

# multiples = [value*3 for value in range(3,31)]
# print(multiples)

# cubes = [value **3 for value in range(1,11)]
# print(cubes)

players = ['charles', 'martina', 'john', 'micheal', 'florence', 'paul', 'eli']
# print("Here are the first four players on my team:")
# for player in players[:4]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_foods[:]

# my_foods.append('fried rice')
# friend_food.append('pasta')

# print("My favorite food are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_food)



print("The first three people are:")
for people in players[:4]:
    print(people.title())

print("Three middle people are:")
for player in players[2:5]:
    print(player.title())

print("The last three items in the list are:")
for human in players[4:]:
    print(human.title())

my_favorite = ['vanilla', 'strawberry', 'blueberry']
friends_favorite = my_favorite[:]

my_favorite.append('blackberry')
friends_favorite.append('chocolate')

print("My Favorite flavors are:")
print(my_favorite)

print("My freind's favorite flavors are:")
print(friends_favorite)