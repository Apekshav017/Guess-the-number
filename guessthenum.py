import random
number = random.randint(1, 100)

print("Welcome to Guess the Number Game!")
print("You have only 5 chances to guess the number.")

chances = 5

while chances > 0:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(" Congratulations! You guessed the correct number.")
        break

    chances -= 1
    print("Remaining chances:", chances)

if chances == 0:
    print(" Game Over! The correct number was:", number)