import random

def roll_dice(playing):
    user_input = input("Rolll the dice? (y/n): ")

    if user_input.lower() == "y":
        print("You rolled: ", random.randint(1, 6), "and", random.randint(1, 6))
        return True
    elif user_input.lower() == "n":
        print("Thanks for playing!")
        return False
    else:
        print("Invalid input. Please try again.")
        return True

while roll_dice(True):    
    pass