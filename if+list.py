requested_toppings = ['mushrooms', 'green-peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green-peppers':
        print("Sorry we are out of green-peppers right now")
    else:
        print(f"Adding {requested_topping} to your pizza")

print("\nFinishing your pizza")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping} to your pizza")
    print("\nFinishing your pizza")
else:
    print("Are you sure you want a plain pizza")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'olives', 'extra cheese']

for requested_topping in requested_toppings:
     if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
     else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

users = ['paul', 'john', 'jim', 'admin', 'rex']
for user in users:
   if user == 'admin':
    print("Hello Admin, would you like to see a status report?")
   else:
    print(f"Hello {user.title()}, thank you for logging in again.")

users = []
if users:
   for user in users:
         print("Hello Admin, would you like to see a status report?")
         print(f"Hello {user.title()}, thank you for logging in again.")
else:
      print(f"We need to find some users!")

current_user = ['paul', 'john', 'jim', 'admin', 'rex']

new_user = ['james', 'peter', 'tim', 'john', 'fred']
for user in new_user:
    if user in current_user:
        print(f"Enter a new user name, {user in new_user} is taken")
    else:
        print("Username is available")