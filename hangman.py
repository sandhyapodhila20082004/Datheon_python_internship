import random

# List of words
words = [
    "python",
    "computer",
    "developer",
    "programming",
    "keyboard",
    "hangman",
    "science",
    "internet",
    "software",
    "technology"
]

# ASCII Hangman stages
hangman_art = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Select a random word
secret_word = random.choice(words).upper()

# Game variables
guessed_letters = set()
wrong_guesses = set()
max_attempts = 6

print("\n================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect attempts.\n")

# Main game loop
while len(wrong_guesses) < max_attempts:

    # Display hangman art
    print(hangman_art[len(wrong_guesses)])

    # Display masked word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong attempts:", len(wrong_guesses), "/", max_attempts)

    # Display previously guessed letters
    print("Guessed letters:", " ".join(sorted(guessed_letters | wrong_guesses)))

    # Check victory
    if all(letter in guessed_letters for letter in secret_word):
        print("\n================================")
        print("       CONGRATULATIONS!")
        print("================================")
        print("You guessed the word:", secret_word)
        print("You WON the game!")
        break

    # Get user input
    guess = input("\nEnter a letter: ").strip().upper()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter. Try another!")
        continue

    # Check the guessed letter
    if guess in secret_word:
        guessed_letters.add(guess)
        print("Correct guess!")
    else:
        wrong_guesses.add(guess)
        print("Wrong guess!")

else:
    print(hangman_art[max_attempts])

    print("\n================================")
    print("          GAME OVER!")
    print("================================")
    print("The correct word was:", secret_word)
    print("You LOST the game!")