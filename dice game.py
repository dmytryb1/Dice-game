import random


def roll_dice():
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    print(x, y)
    dice_game(x, y)


def dice_game(x, y):
    if x + y == 7 or x == y:
        print("Winner!!!")
        play_again()
    else:
        print("You Lose")
        play_again()


def play_again():
    choice = input("Type in   y   to play again, and any key to quit:  ")
    if choice == "y":
        roll_dice()
    else:
        print("Thank you for playing")

roll_dice()
