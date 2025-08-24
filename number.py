import random


def main_menu():
    print("\n=== Welcome to Number Guesser! ===")
    print("Select a level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Close")

def play_game(max_number, max_attempts):
    number_to_guess = random.randint(1, max_number)
    attempts = 0

    print("\nI'm thinking of a number. Can you guess it?")
    print(f"It's between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print(f"Please enter a valid number between 1 and {max_number}.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"🎉 You got it in {attempts} attempts! Great job!")
            return
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print(f"😢 You're out of attempts. The number was {number_to_guess}.")

def number_guesser():
    while True:
        main_menu()
        choice = input("\nChoose your mode (1-4): ")

        if choice == "1":
            play_game(max_number=10, max_attempts=5)
        elif choice == "2":
            play_game(max_number=50, max_attempts=7)
        elif choice == "3":
            play_game(max_number=100, max_attempts=10)
        elif choice == "4":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid input. Please choose again.")

if __name__ == "__main__":
    number_guesser()
