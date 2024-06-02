import random


def GuessTheNumber():
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("guess the correct random number between 1 and 100: "))

        if guess == secret_number:
            print("You win the Game !!!")
            break
        elif guess < secret_number:
            print("Too low. try again ")
        else:
            print("Too high. try again ")


GuessTheNumber()
