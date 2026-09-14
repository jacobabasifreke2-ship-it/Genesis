# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)
# # this is me trying it myself
# freinds = ['Paul', 'Mark', 'Henry', 'Caleb', 'Joshua', 'Adam']
# print(freinds[0])
# print(freinds[1])
# print(freinds[2])
# print(freinds[3])
# print(freinds[4])
# print(freinds[5])

# text = f"hello {freinds[1]} how are you"
# print(text.title())

# motorcycles = ['honda', 'yamaha','suzuki']
# print(motorcycles)

# motorcycles.insert(2 ,'ducati')
# print(motorcycles)

# del motorcycles[3]
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# last_owned = motorcycles.pop(1)
# print(f"The last motorcycle I owned was a {last_owned.title()}")

# too_expensive = 'honda'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive} is too expensive for me")

invited = ['Wilson', 'Fredrick', 'Promise']
del invited[1]
invited.insert(1 ,'Joshua')
invited.insert(3, 'Charles')
invited.insert(4, 'Isaac')
invited.append('John')

popped_invited = invited.pop(2)
popped_invited = invited.pop(2)
popped_invited = invited.pop(1)
popped_invited = invited.pop(1)
print(f"Miss {invited[0]}, I personally invite you to an elaborate dinner")
print(f"Master {invited[1]}, I personally invite you to an elaborate dinner")
# print(f"Master {invited[2]}, I personally invite you to an elaborate dinner")
# print(f"Master {invited[3]}, I personally invite you to an elaborate dinner")
# print(f"Master {invited[4]}, I personally invite you to an elaborate dinner")
# print(f"Master {invited[5]}, I personally invite you to an elaborate dinner")
print(f"I am dearly sorry Master {invited.pop(2)} but the dinner is being cancelled ")
print(f"I am dearly sorry Master {invited.pop(2)} but the dinner is being cancelled ")
print(f"I am dearly sorry Master {invited.pop(3)} but the dinner is being cancelled ")
print(f"I am dearly sorry Master {invited.pop(2)} but the dinner is being cancelled ")
del invited[0]
del invited[0]
print(invited)