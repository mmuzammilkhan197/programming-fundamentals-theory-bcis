secret = 47      # secret number between 1 and 100
attempts = 0
guess = 0

# Keep asking until the guess matches
while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")

print("Total attempts:", attempts)