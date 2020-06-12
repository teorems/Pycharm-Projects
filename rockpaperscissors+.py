# Write your code here
import random

print("Enter your name:", end=" ")
name = input()
print("Hello,", name)

rating = open("rating.txt", "r")
rating = rating.readlines()
for line in rating:
    if name in line:
        score = int(line.split()[1])

else:
    score = 0


keys = input("Enter the keys :").split(',')
if not any(keys):
    keys = ["rock", "paper", "scissors"]
print("Okay, let's start")

while True:

    user_choice = input()

    if user_choice in keys:
        computer = random.choice(keys)
        new_keys = keys[keys.index(user_choice) + 1:] + keys[0:keys.index(user_choice)]
        if user_choice == computer:
            print("There is a draw ({})".format(user_choice))
            score += 50
        elif new_keys.index(computer) < len(new_keys) / 2:
            print("Sorry, but computer chose {}".format(computer))

        else:
            print("Well done. Computer chose {} and failed.".format(computer))
            score += 100
    elif user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(score)
    else:
        print("Invalid input")
