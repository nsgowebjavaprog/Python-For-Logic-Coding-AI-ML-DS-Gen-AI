import random

lowest = 1
highest = 100

random_number = random.randint(lowest, highest)
# print(random_number)

guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lowest} and {highest}.")

while is_running:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {guesses} guesses.")
            is_running = False
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        
print("Game Over. Thanks for playing!")
