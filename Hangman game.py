import random

# 1. List of words
words = ["python", "computer", "developer", "coding", "program"]

# 2. Select a random word
word = random.choice(words)

# 3. Game variables
guessed_letters = set()
wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")

# 4. Game loop
while wrong_guesses < max_wrong:

    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    # Check if player won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word! 🎉")
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store guessed letter
    guessed_letters.add(guess)

    # Check correct or wrong
    if guess in word:
        print("Correct guess! ✅")
    else:
        print("Wrong guess! ❌")
        wrong_guesses += 1

# 5. Lose condition
if wrong_guesses == max_wrong:
    print("\nGame Over! 😢")
    print("The word was:", word)