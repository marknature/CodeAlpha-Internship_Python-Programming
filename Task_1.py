import random

# Predefined list of words
word_list = ['apple', 'banana', 'grape', 'orange', 'peach']

# Randomly select a word
word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)
guessed_letters = []  # To store letters the user has guessed
attempts_left = 6

# Function to display current progress
def display_word():
    display = ''
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.")

# Main game loop
while attempts_left > 0:
    print("\n" + display_word())
    guess = input("Enter a letter: ").lower()

    # Input validation: make sure the user inputs a single alphabetic character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good job! The letter is in the word.")
    else:
        attempts_left -= 1
        print(f"Wrong guess. You have {attempts_left} attempts left.")

    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\nCongratulations! You guessed the word:", word_to_guess)
        break

# If player runs out of attempts
if attempts_left == 0:
    print("\nGame Over! The word was:", word_to_guess)
