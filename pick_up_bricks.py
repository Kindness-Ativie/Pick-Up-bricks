import random

print("Virtual Pick UP Bricks 🤨")
print("INSTRUCTIONS: Pick up 1 or 2 bricks. Last person to pick up bricks wins.")

number_of_bricks = int(input("How many bricks would you like to play with?: "))

player_1 = str(input("What is the name of player 1?: "))
player_2 = str(input("What is the name of player 2?: "))

coin_flip = random.randint(1, 2)

if coin_flip == 1:
    first_player = player_1
    second_player = player_2
    print(f"{player_1}, you're up first.")
else:
    first_player = player_2
    second_player = player_1
    print(f"{player_2}, you're up first.")

print("")
print(f"GAME BEGINS 🤪")
print('|' * number_of_bricks)


while number_of_bricks > 0:
    subtraction_number = int(input(f"Take 1 or 2 bricks, {first_player}. 👀: "))
    number_of_bricks = number_of_bricks - subtraction_number
    print('|' * number_of_bricks)
    print(f"Total bricks remaining: {number_of_bricks}")

    print("")

    subtraction_number = int(input(f"Take 1 or 2 bricks, {second_player}. 👀: "))
    number_of_bricks = number_of_bricks - subtraction_number
    print('|' * number_of_bricks)
    print(f"Total bricks remaining: {number_of_bricks}")


print("Game OVER! Pile empty. LAST MOVE WON.")