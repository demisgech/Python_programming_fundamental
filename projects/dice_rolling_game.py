import random

def dice_rolling_game():
    dice = {}
    num_of_dice = int(input("How many dice you want to roll? : "))
    while(True):
        for x in range(num_of_dice):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            dice[F"die {x + 1}"] = [die1,die2]
        response:str = input("Roll the dice? (y/n): ")
        if(response.upper() == 'Y'):
            print(dice)
        elif response.upper() == 'N':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")
        dice = {}

dice_rolling_game()

# dice = {}

# for x in range(5):
#     die1 = random.randint(1,6)
#     die2 = random.randint(1,6)
  
#     dice[x] = [die1,die2]

# print(dice)