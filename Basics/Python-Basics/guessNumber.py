guess_count = 0
guess_limit = 5
secretNumber = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secretNumber:
        print(f"You've got {guess_limit - guess_count + 1}"
              f" points out of { guess_limit}")
        break
    elif guess_count != guess_limit:
        print(f"You've {guess_limit - guess_count}  chances. Please,try again!")
    else:
        print("Sorry, you have failed!")

