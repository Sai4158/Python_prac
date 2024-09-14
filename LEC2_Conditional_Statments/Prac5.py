num = int(input("enter a number (0-10): "))

if  num >10:
    print("enter below 10")
elif num <0:
    print("Please enter from 0 to 10: ")
else: 
    print("goood")


# Generate a random number
import random
random_num = random.randint(0, 10)

if num == random_num:
    print("You correctly guessed the number!")
else:
    print(f"Sorry, the correct number was {random_num}")