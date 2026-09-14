alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# print(alien_0)

# alien_0['x_position'] = 38
# alien_0['y_position'] = 25
# print(alien_0)


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'faa'}
# print(f"Original position: {alien_0['x_position']}")
# alien_0['speed'] = 'medium'

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 2
# elif alien_0['speed'] == 'medium':
#     x_increment = 4
# else:
#     # This must be a fast alien.
#     x_increment = 6
    
# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['color'] 
# print(alien_0)

# best_city = {
#     'paul': 'texas',
#     'john': 'los angeles',
#     'joy': 'texas',
#     'henry': 'new orleans',
#     }

# city = best_city['john'].title()
# print(f"John's best city to visit is {city}")

# alien_0 = {'color': 'green', 'points': 5,} #'speed': 'slow'
# point_value = alien_0.get('speed', 'No speed value placed.')
# print(point_value)

# player004 = {
#     'avater': 'noob',
#     'power': 'super',
#     'weapon': 'sickle'
# }

# for key, value in player004.items():
#     print(f"\n Key: {key}")
#     print(f"Value: {value}")

# for name, city in best_city.items():
#     print(f"{name.title()}'s best city suggestion to travel to is {city.title()}.")

# for name in best_city.keys():
#     print(name.title())
# for city in best_city.values():
#     print(city.title())

# friends = ['paul', 'joy']
# for name in best_city.keys():
#     print(f"Hi {name.title()}")

#     if name in friends:
#         city = best_city[name].title()
#         print(f"\t{name.title()},I see you fancy {city}")
    
#     if 'peter' not in best_city.keys():
#         print("Peter, please pick a city")
#     if 'john' in best_city.keys():
#         print('Thank you John for making a vote')

# for name in sorted(best_city.keys()):
#     print(f"{name.title()}, thank you for voting.")

# print("The following cities has been mentioned:")
# for city in set(best_city.values()):
#     print(city.title())

# rivers = {
#     'effiel tower': 'paris',
#     'white house': 'white house',
#     'colloseum': 'italy',
#     'leaning tower': 'london',
#     'mount olympus': 'greece',
# }

# for city, cites in rivers.items():
#     print(f"The famous {city.title()} is located in {cites.title()}")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(30):
#     begin_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
#     aliens.append(begin_alien)
#     old_alien = {'color': 'yellow', 'points': '10', 'speed': 'medium'}
#     aliens.append(old_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print(f"\nTotal number of aliens: {len(aliens)}")

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],x

# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

# for topping in  pizza['toppings']:
#     print(topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
#     }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()} favorite languages are:")
#     for language in languages:
#         print(f"{language.title()}")

# # students = {
# #     'john': {
# #         'class': 'JSS3',
# #         'grade': 'B+',
# #         'dob': '12 june 2000',
# #     },

# #     'henry': {
# #         'class': 'SSS3',
# #         'grade': 'A++',
# #         'dob': '3 august 1950'
# #     }
# # }

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#         },
        
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         },
#     }
# for username, user_info in users.items():
#      print(f"\nUsername: {username}")
#      full_name = f"{user_info['first']} {user_info['last']}"
#      location = user_info['location']

#      print(f"\tFull name: {full_name.title()}")
#      print(f"\tLocation: {location.title()}")

# people = {
#     'Agent001': {
#         'full_name' : 'paul',
#         'last_name' : 'peter',
#         'age': '18',
#         'location': 'san fransisco',
#         'speed': 'fast',
#     },

#     'Agent002': {
#         'full_name' : 'helen', 
#         'last_name' : 'james',
#         'age': '16',
#         'location': 'los angeles',
#         'speed': 'medium',
#     }
# }
# for name, details in people.items():
#     print(f"This is what I know about {name.title()}")
#     full_names = f"{details['full_name']} {details['last_name']}"
#     print(f"Full names: {full_names.title()}")
#     print(f"Age: {details['age'].title()} \nLocation: {details['location'].title()} \nSpeed: {details['speed'].title()}")