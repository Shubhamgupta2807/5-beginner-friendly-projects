"""
Password Guessing Game (Beginner Python Project)

This is a simple command-line game built using Python.
The player selects a difficulty level (Easy, Medium, Hard), and the program
randomly chooses a secret word based on the selected level.

The player has limited attempts to guess the correct password.
After each wrong guess, a hint is shown to help the player.

Concepts used:
- Python lists
- Random module
- Conditional statements
- Loops
- String comparison
- User input handling

This project is great for beginners to practice Python basics.
"""

import random

# level define..

# Easy (words)
name_words = [
    "shubh","yash","shiv","ansh","bhanu","isha","khus","bunty","priya","ajay"
]
# Medium (words)
city_words = [
    "ujjain","jaora","nimach","alot","namli","nagda","indore","bhopal","sagar","dewas"
]
# Hard (words)
country_words = [
    "india","russia","brazil","china","srilanka","america","pakistan","canada","japan","egypt"
]

print("--Welcome to the password guessing game--\n")
level = input("Enter choice -(Easy  medium  hard) = ").lower()

if level == "easy":
    secret = random.choice(name_words)
elif level == "medium":
    secret = random.choice(city_words)
elif level == "hard":
    secret = random.choice(country_words)
else:
    print("Invalid input! Defalut choice is Easy.")
    secret = random.choice(name_words)
max_attempt =5
attempts = 0
print("\nGuess the secret password")
print(f"Your choose level is {level}")

while True:
    guess = input("Enter your guess : =").lower()
    attempts +=1
    if guess == secret:
        print(f"congrats you guess a password {secret} in {attempts} attemts!")
        break

    if attempts ==max_attempt:
        print(f"Your maximum guessing limit {max_attempt} is over!")
        print(f"Your password is {secret}")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print(f"hint - {hint}")
print("Game over!")
