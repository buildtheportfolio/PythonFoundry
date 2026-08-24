import random


def main():
    secret = random.randint(1, 10)
    print("Number Guessing Game")
    print("Guess a number between 1 and 10.")

    while True:
        guess = input("Your guess: ").strip()

        if not guess.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess)

        if guess == secret:
            print("Correct! You guessed it.")
            break
        if guess < secret:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


if __name__ == "__main__":
    main()
