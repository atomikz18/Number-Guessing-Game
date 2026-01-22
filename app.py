import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Please select the difficulty level: ")
if level == "1":
    print("Great! You have selected the Easy difficulty level.")
    print("You have 10 chances!")
    chances = 10
elif level == "2":
    print("Great! You have selected the Medium difficulty level.")
    print("You have 5 chances!")
    chances = 5
elif level == "3":
    print("Great! You have selected the Hard difficulty level.")
    print("You have 3 chances!")
    chances = 3
else:
    print("That level isn't available")
    exit()


x = random.randint(1, 100)
while chances > 0:
    guess = int(input("Enter your guess: "))
    chances -= 1
    if guess == x:
        print("You have won!!")
        break
    elif guess > x:
        print("Too high!")
    elif guess < x:
        print("Too low!")
    if chances == 0:
        print(f"Sorry you failed.. The number was {x}")
