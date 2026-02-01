import random

# Ask user for range
start = int(input("🎯 Enter the starting value of the range: "))
end = int(input("🎯 Enter the ending value of the range: "))

# Generate random number
secret_number = random.randint(start, end)

# Flags
is_correct = False
reveal_answer = False

print("\n🔢 Welcome to the Number Guessing Game!")
print(f"Guess the number between {start} and {end}.\n")

while not is_correct:

    if reveal_answer:
        print(f"✅ The correct number was: {secret_number}")
        break

    # User guess
    guess = int(input("👉 Enter your guess: "))

    if guess != secret_number:  # Incorrect guess
        if guess > secret_number:
            print(f"❌ {guess} is too high.")
        else:
            print(f"❌ {guess} is too low.")

        # Ask if user wants to reveal the answer
        reveal_answer = input("🤔 Do you want to reveal the answer? (True/False): ").strip().lower() == "true"

    else:  # Correct guess
        is_correct = True

else:
    print(f"🎉 Correct! The number was {secret_number}. Well done! 🎉")