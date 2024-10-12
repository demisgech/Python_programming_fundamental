import random

def number_guessing_game():
    computer_guess = random.randint(1,100)
    while True:
        user_guess = int(input("Guess the number 1 and 100!: "))
        
        if computer_guess < user_guess:
            print('Too high!')
        elif computer_guess > user_guess:
            print("Too low!")
        else:
            print('Great! You win!')
            break

number_guessing_game()