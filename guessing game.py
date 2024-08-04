import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guessed_correctly = False

    # Loop until the player guesses the correct number
    while not guessed_correctly:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        number_of_attempts += 1
        # Compare the guess to the selected number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
