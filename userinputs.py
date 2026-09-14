# name = input('Please enter your name: ')
# print(f"\nHello, {name}!")

# prompt = 'If you tell us what you do we can personalize the ads you see'
# prompt += '\nWhat is your first name'

# name = input( prompt)
# print(f"\nHello, {name.title()}!")

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# rental = input("Which type of car would you like? ")
# print(f"Let me see if I can get you a {rental.title()}")

# total = input("How many people are in your dining group? ")
# total = int(total)

# if total >= 8:
#     print("Sorry but you'll have to wait for a table")
# else:
#     print("We have a table ready!")

weight = input("How much do you weigh? ")
weight = int(weight)

if weight >= 60:
    print(f"\nYou are a little bit over the weight limit \nHow about you try another ride")
else:
    print(f"\nYou are fit to get in the ride")