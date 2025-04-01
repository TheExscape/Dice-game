import random



input("Welcome to dice game, type roll to start game: ")



dice_outcomes = [1, 2, 3, 4, 5]


player_outcomes = "player"
print(player_outcomes)
print(random.randrange(1, 6)) #random for player




computer_outcomes = "computer"
print(computer_outcomes)
print(random.randrange(1, 6)) #random for computer


if computer_outcomes == player_outcomes:
    print("tie")
else:
    print("no")