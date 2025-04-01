import random
import time

user_text = str(input("Welcome to dice game, type roll to start game: "))


while user_text != "roll":
    print("You did not enter roll")
    user_text = input("please try again: ")
else:
    print("You rolled the die")


player_outcome = random.randrange(1, 6)
computer_outcome = random.randrange(1, 6)

print(player_outcome) #random for player

for seconds in range(3, 0, -1): #this is a count down for the timer between the player roll and computer roll 
    time.sleep(1)

print()

print("Computer rolls the die")


print(computer_outcome) #random for computer

for seconds in range(3, 0, -1):
    time.sleep(1)

print()

if player_outcome == computer_outcome:
    print("You guys tie")
elif player_outcome > computer_outcome:
    print("You win")
elif player_outcome < computer_outcome:
    print("You lost")

