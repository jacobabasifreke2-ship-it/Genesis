# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 2

prompt = "Tell me what you what me to repeat to you"
prompt += "Enter quit to end the program"
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

info = f"\nSalutations user, how mayy I be of service"
info += f"\nInput your username to get your login pin"
info += f"\nEnter end to terminate the program: "

message = ""
import random
man = random.randint(34324,58958)

while message != 'end':
    message = input(info)
    if message == 'paul@gmail':
        message = man
    else:
        message = "Please check the username and try again"
    if message != 'end':
        print(message)

#The above code was to run a program that produces a login pin once a username has been entered, the program was meant to terminate once end was entered, the program was meant to restrict all entries without a "@gmail" attached to it but currently can't be completed

# info = f"\nEnter your age to get the year you were born in "
# info += f"\nTo terminate the program enter end"
# info += f"\nEnter your age^_+ :"

# prompt = f"\nPlease enter the name of a city you have visited:"
# prompt += f"\n(Enter 'end' when you are finished.)" 
# prompt += f"\n"

# while True:
#     city = input(prompt)

#     if city == 'end':
#         break

#     elif city == 'New York' or 'California' or 'New Orleans':
#         print(f"Oh I've been to {city.title()} already")
#     if False:
#         print(f"Oh so you have been to {city.title()}")
#         print(f"I think I'll visit {city.title()} someday!")

# current_number = 0
# while current_number < 10:
#     current_number =+ 1                   #You don't understand "continue" function 
#     if current_number % 2 == 0:            #remember to check it again
#         continue
#     print(current_number)


prompt = f"\nHello Welcome to Genesis Ciniema"
prompt += f"\nWe'll be showing 'Infinite' today"
prompt += f"\nAre you here alone or with company: "

ans1 = ("Enter your age to know the cost of your movie ticket: ")
ans2 = ("What is the number of your companions: ")
data = input(prompt)
info = int(input(ans2))
message = int(input(ans1))


# message = int(input(ans1))
if data == "alone":
    print(input(ans1))
elif data == "company":
    print(input(ans2))
else:
    print("Please choose a vaild option!")

 #perform a check
if info <= 9:
    print("Enter your ages to know the costs of your movie tickets")
else:
    print("Please enter the number of your companions")

#perform another check
if message < 3:
    print("Congratulations young one your ticket is free")
elif message < 12:
    print("Your ticket costs only $10")
elif message < 18:
    print("Your ticket costs only $15")
elif message < 30:
    print("Your ticket costs only $20")
elif message < 85:
    print("Your ticket costs only $25")
elif message <= 101:
    print("Your ticket costs only $10")
elif message > 101:
    print("Please enter a valid age")
else:
    print("Kindly enter a valid number")