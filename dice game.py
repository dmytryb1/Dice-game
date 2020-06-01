import random
dice1 = random.randint(1, 8)
dice2 = random.randint(1, 8)
print(dice1)
print(dice2)
if dice1 + dice2 == 7:
    print("Winner!!!")
elif dice1 == dice2:
    print("Winner!!!")
else:
    print("You Lose")